# Generated by Django 4.1.7 on 2023-04-11 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0002_alter_badge_created_alter_reviewrating_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 11, 6, 55, 23, 392478, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 11, 6, 55, 23, 394532, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
