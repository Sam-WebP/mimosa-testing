from decimal import Decimal

import stripe
from django.conf import settings
from django.db import models

from core.models.tax_rate import TaxRate


class StripeProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.ForeignKey(
        TaxRate, on_delete=models.SET_NULL, null=True, blank=True
    )

    stripe_product_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True

    def stripe_save_sync(self=models, *args, **kwargs):
        is_new = self.pk is None
        manager = self.__class__._default_manager
        record_new = self

        if is_new:
            record_old = None
        else:
            record_old = manager.get(pk=self.pk)

        # Must save first so a PK is available for Stripe.
        super(StripeProduct, self).save(*args, **kwargs)

        if record_old is None:
            sync_product_id, sync_price_id = sync_to_stripe_new(
                name_new=record_new.name,
                price_new=record_new.price,
                pk=str(record_new.pk),
                model_name=record_new.__class__.__name__.lower(),
                tax_rate=record_new.tax_rate,
            )
        else:
            sync_product_id, sync_price_id = sync_to_stripe_existing(
                product_id=record_old.stripe_product_id,
                price_id=record_old.stripe_price_id,
                name_new=record_new.name,
                name_old=record_old.name,
                price_new=record_new.price,
                price_old=record_old.price,
                tax_rate_new=record_new.tax_rate,
                tax_rate_old=record_old.tax_rate,
            )

        self.stripe_product_id = sync_product_id
        self.stripe_price_id = sync_price_id

        # Must save Stripe IDs to DB.
        super(StripeProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


def sync_to_stripe_new(
    name_new: str,
    price_new: Decimal,
    pk: str,
    model_name: str,
    tax_rate: TaxRate = None,
):
    stripe_product = stripe.Product.create(
        name=name_new, metadata={model_name + "_pk": pk}
    )

    price_cents = int(price_new * 100)
    price_data = {
        "product": stripe_product.stripe_id,
        "unit_amount": price_cents,  # Stripe expects the amount in cents
        "currency": settings.STRIPE_CURRENCY,
    }

    if tax_rate and tax_rate.stripe_tax_rate_id:
        price_data["tax_behavior"] = "exclusive"
        price_data["metadata"] = {"tax_rate": tax_rate.stripe_tax_rate_id}

    stripe_price = stripe.Price.create(**price_data)

    return stripe_product.stripe_id, stripe_price.stripe_id


def sync_to_stripe_existing(
    product_id: str,
    price_id: str,
    price_new: Decimal,
    price_old: Decimal,
    name_new: str,
    name_old: str,
    tax_rate_new: TaxRate = None,
    tax_rate_old: TaxRate = None,
):
    price_id_new = price_id
    price_new_cents = int(price_new * 100)

    if name_old != name_new:
        stripe.Product.modify(product_id, name=name_new)

    if price_old != price_new or tax_rate_new != tax_rate_old:
        stripe.Price.modify(price_id, active=False)

        price_data = {
            "product": product_id,
            "unit_amount": price_new_cents,
            "currency": settings.STRIPE_CURRENCY,
        }

        if tax_rate_new and tax_rate_new.stripe_tax_rate_id:
            price_data["tax_behavior"] = "exclusive"
            price_data["metadata"] = {
                "tax_rate": tax_rate_new.stripe_tax_rate_id
            }

        price_id_new = stripe.Price.create(**price_data).stripe_id

    return product_id, price_id_new
