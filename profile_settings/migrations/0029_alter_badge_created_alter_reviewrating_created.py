# Generated by Django 4.1.7 on 2023-05-07 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0028_alter_badge_created_alter_reviewrating_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 12, 36, 27, 344010, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 12, 36, 27, 346074, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
