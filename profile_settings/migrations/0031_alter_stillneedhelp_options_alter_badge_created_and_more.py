# Generated by Django 4.1.7 on 2023-05-10 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_settings", "0030_alter_badge_created_alter_reviewrating_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="stillneedhelp",
            options={"verbose_name_plural": "Still Need Helps"},
        ),
        migrations.AlterField(
            model_name="badge",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 984170, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 986053, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]