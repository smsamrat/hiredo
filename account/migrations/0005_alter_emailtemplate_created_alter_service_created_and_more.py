# Generated by Django 4.1.7 on 2023-04-16 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_emailtemplate_created_alter_service_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 47, 5, 154478, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 47, 5, 152930, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 47, 5, 154053, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]