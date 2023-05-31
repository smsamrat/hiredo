# Generated by Django 4.1.7 on 2023-05-23 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0043_alter_emailtemplate_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 9, 28, 3, 248223, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 9, 28, 3, 246482, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 9, 28, 3, 247775, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]