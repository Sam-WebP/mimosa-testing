# Generated by Django 5.0.3 on 2024-08-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0030_merge_20240809_0136"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordersessionline",
            name="tax_amount_certificate",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10
            ),
        ),
        migrations.AddField(
            model_name="ordersessionline",
            name="tax_amount_fee",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10
            ),
        ),
    ]