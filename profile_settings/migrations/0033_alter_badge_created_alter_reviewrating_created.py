# Generated by Django 4.1.7 on 2023-05-22 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0032_alter_badge_created_alter_reviewrating_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 22, 8, 54, 20, 954521, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 22, 8, 54, 20, 964087, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
