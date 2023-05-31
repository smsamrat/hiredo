# Generated by Django 4.1.7 on 2023-04-18 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0004_alter_setcreditpurchased_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 18, 10, 39, 29, 848097, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 18, 10, 39, 29, 848122, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 18, 10, 39, 29, 847027, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 18, 10, 39, 29, 847065, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]