# Generated by Django 5.0.1 on 2024-02-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_uploadtask_sourcedocument_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadtask",
            name="metadata",
            field=models.JSONField(default=dict, verbose_name="Metadata"),
        ),
    ]
