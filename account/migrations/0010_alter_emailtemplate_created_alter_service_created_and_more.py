# Generated by Django 4.1.7 on 2023-04-17 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0009_alter_emailtemplate_created_alter_service_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 17, 8, 11, 43, 261153, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 17, 8, 11, 43, 259656, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 17, 8, 11, 43, 260726, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
