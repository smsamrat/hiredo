# Generated by Django 4.1.7 on 2023-05-07 06:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0024_user_stripe_customerid_alter_emailtemplate_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 6, 38, 11, 975290, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 6, 38, 11, 973047, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="smstemplate",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 6, 38, 11, 974814, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
