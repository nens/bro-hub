# Generated by Django 5.0.1 on 2024-02-21 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0014_remove_importtask_organisation_and_more"),
        ("gmn", "0011_delete_gmnstartregistration"),
    ]

    operations = [
        migrations.AddField(
            model_name="gmn",
            name="data_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.organisation",
            ),
        ),
        migrations.AddField(
            model_name="measuringpoint",
            name="data_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.organisation",
            ),
        ),
    ]
