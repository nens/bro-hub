# Generated by Django 5.0.1 on 2024-02-21 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gmn", "0012_gmn_data_owner_measuringpoint_data_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measuringpoint",
            name="gmn",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gmn.gmn",
            ),
        ),
    ]
