# Generated by Django 5.0.1 on 2024-02-06 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gmn", "0004_remove_measuringpoint_tube_gml_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="measuringpoint",
            name="gmn",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="gmn.gmn",
            ),
        ),
    ]
