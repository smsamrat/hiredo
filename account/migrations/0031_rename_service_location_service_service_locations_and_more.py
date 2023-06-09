# Generated by Django 4.1.7 on 2023-05-07 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "account",
            "0030_alter_emailtemplate_created_alter_service_created_at_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="service_location",
            new_name="service_locations",
        ),
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 37, 48, 832012, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 37, 48, 830082, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 37, 48, 831433, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
