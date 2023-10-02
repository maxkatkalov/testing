# Generated by Django 4.2.5 on 2023-10-01 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("staff_app", "0004_alter_position_name_alter_staffuser_reporting_to"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="companies",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(
                default="Unnamed position 2023-10-01 20:12:29.432431",
                max_length=156,
                unique=True,
            ),
        ),
    ]
