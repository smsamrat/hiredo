# Generated by Django 4.1.7 on 2023-05-05 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0008_alter_creditpurchasedbyuser_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 56, 14, 797992, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 56, 14, 798007, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 56, 14, 797351, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 56, 14, 797372, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
