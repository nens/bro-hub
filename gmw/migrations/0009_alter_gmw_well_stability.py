# Generated by Django 5.0.1 on 2024-03-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gmw", "0008_alter_monitoringtube_tube_top_diameter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gmw",
            name="well_stability",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
