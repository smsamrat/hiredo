# Generated by Django 4.1.7 on 2023-04-17 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0010_alter_badge_created_alter_reviewrating_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 17, 9, 34, 17, 450884, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 17, 9, 34, 17, 452857, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
