# Generated by Django 5.0.3 on 2024-07-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_alter_order_order_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="logos/"
                    ),
                ),
            ],
            options={
                "verbose_name": "Setting",
                "verbose_name_plural": "Settings",
            },
        ),
    ]
