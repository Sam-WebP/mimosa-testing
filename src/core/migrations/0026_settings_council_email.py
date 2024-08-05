# Generated by Django 5.0.3 on 2024-07-30 07:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="council_email",
            field=models.EmailField(
                blank=True,
                help_text="Email for sending customers order notifications",
                max_length=254,
                null=True,
                validators=[django.core.validators.EmailValidator()],
            ),
        ),
    ]