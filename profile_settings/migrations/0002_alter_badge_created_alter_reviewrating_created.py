# Generated by Django 4.1.7 on 2023-04-11 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 11, 6, 53, 41, 433177, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 11, 6, 53, 41, 435082, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
