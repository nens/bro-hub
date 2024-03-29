# Generated by Django 5.0.1 on 2024-02-20 11:31

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GMW",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("bro_id", models.CharField(max_length=18)),
                (
                    "delivery_accountable_party",
                    models.CharField(blank=True, max_length=8, null=True),
                ),
                (
                    "quality_regime",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "delivery_context",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "construction_standard",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "initial_function",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("removed", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "ground_level_stable",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "well_stability",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("nitg_code", models.CharField(blank=True, max_length=100, null=True)),
                ("well_code", models.CharField(blank=True, max_length=100, null=True)),
                ("owner", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "well_head_protector",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "delivery_location",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "delivered_vertical_postition",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "standardized_location",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "object_registration_time",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "registration_status",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "GMW's",
            },
        ),
        migrations.CreateModel(
            name="MonitoringTube",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "tube_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("tube_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "artesian_well_cap_present",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "number_of_geo_ohm_cables",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_top_diameter",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "variable_diameter",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_status",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_top_position",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_top_positioning_method",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_part_inserted",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_in_use",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_packing_material",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "tube_material",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("glue", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "screen_length",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "sock_material",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "screen_top_position",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "screen_bottom_position",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "plain_tube_part_length",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "gmw",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gmw.gmw",
                    ),
                ),
            ],
        ),
    ]
