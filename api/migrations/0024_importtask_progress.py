# Generated by Django 5.0.1 on 2024-03-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0023_uploadtask_bro_id_alter_uploadtask_registration_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="importtask",
            name="progress",
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]