# Generated by Django 5.0.1 on 2024-03-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gmw", "0007_alter_gmw_construction_standard_alter_gmw_data_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monitoringtube",
            name="tube_top_diameter",
            field=models.CharField(max_length=100, null=True),
        ),
    ]