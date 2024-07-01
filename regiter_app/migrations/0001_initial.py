# Generated by Django 5.0.6 on 2024-06-30 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClassUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("class_name", models.CharField(max_length=44)),
            ],
            options={
                "verbose_name": "Class",
                "db_table": "Class_table",
            },
        ),
        migrations.CreateModel(
            name="RegionUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("region_name", models.CharField(max_length=99)),
            ],
            options={
                "verbose_name": "Region",
                "db_table": "Region_table",
            },
        ),
        migrations.CreateModel(
            name="UserInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("phone_your", models.CharField(max_length=13)),
                (
                    "class_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="regiter_app.classuser",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="regiter_app.regionuser",
                    ),
                ),
            ],
            options={
                "verbose_name": "User_information",
                "db_table": "user_table",
            },
        ),
    ]