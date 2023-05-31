# Generated by Django 4.1.7 on 2023-05-07 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "account",
            "0023_alter_emailtemplate_created_alter_service_created_at_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="stripe_customerId",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 6, 19, 49, 5163, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 6, 19, 49, 3001, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 6, 19, 49, 4647, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
