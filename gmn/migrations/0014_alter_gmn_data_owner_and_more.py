# Generated by Django 5.0.1 on 2024-03-12 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0019_remove_importtask_created_at_and_more"),
        ("gmn", "0013_alter_measuringpoint_gmn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gmn",
            name="data_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.organisation"
            ),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="delivery_accountable_party",
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="delivery_context",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="groundwater_aspect",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="monitoring_purpose",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="object_registration_time",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="quality_regime",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="registration_status",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="gmn",
            name="start_date_monitoring",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="data_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.organisation"
            ),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="gmn",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="gmn.gmn"
            ),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="gmw_bro_id",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="measuringpoint_code",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="measuringpoint_start_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="tube_number",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="measuringpoint",
            name="tube_start_date",
            field=models.DateField(),
        ),
    ]
