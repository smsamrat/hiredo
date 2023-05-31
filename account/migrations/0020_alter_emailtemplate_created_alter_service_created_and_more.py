# Generated by Django 4.1.7 on 2023-05-03 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0019_alter_emailtemplate_created_alter_service_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 857912, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 856296, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 857405, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]