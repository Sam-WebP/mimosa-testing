# Generated by Django 5.0.3 on 2024-09-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0032_certificate_child_certificates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="assessment",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="property",
            name="deposited_plan",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="property",
            name="lot",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="property",
            name="section",
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
