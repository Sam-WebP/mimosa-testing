# Generated by Django 5.0.3 on 2024-08-06 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_ordersession_customer_address_country_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="stripe_checkout_id",
        ),
    ]