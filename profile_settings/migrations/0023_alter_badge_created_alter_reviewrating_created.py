# Generated by Django 4.1.7 on 2023-05-06 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0022_alter_badge_created_alter_reviewrating_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 6, 11, 13, 27, 41403, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 6, 11, 13, 27, 44946, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
