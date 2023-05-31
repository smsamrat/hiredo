# Generated by Django 4.1.7 on 2023-04-16 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_emailtemplate_created_alter_service_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 56, 47, 190502, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 56, 47, 188061, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 56, 47, 189803, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]