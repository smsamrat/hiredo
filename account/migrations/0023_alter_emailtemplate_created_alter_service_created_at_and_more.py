# Generated by Django 4.1.7 on 2023-05-06 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "account",
            "0022_alter_emailtemplate_created_alter_service_created_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 6, 11, 13, 27, 20669, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 6, 11, 13, 27, 16948, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 6, 11, 13, 27, 19868, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
