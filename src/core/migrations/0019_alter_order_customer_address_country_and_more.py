# Generated by Django 5.0.3 on 2024-07-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_order_stripe_payment_intent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="customer_address_country",
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_address_post_code",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_address_state",
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_address_street_line_1",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_address_street_line_2",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_address_suburb",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_company_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_company_ref",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="stripe_payment_intent",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
