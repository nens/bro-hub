# Generated by Django 5.0.1 on 2024-02-06 10:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("gmn", "0003_rename_measuring_point_code_measuringpoint_measuringpoint_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="measuringpoint",
            name="tube_gml_id",
        ),
    ]
