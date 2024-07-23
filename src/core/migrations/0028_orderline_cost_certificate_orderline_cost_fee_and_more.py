# Generated by Django 5.0.3 on 2024-07-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_alter_orderline_certificate_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderline",
            name="cost_certificate",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderline",
            name="cost_fee",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="ordersessionline",
            name="cost_certificate",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ordersessionline",
            name="cost_fee",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
