# Generated by Django 4.1.7 on 2023-05-22 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0020_alter_creditpurchasedbyuser_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 22, 8, 54, 21, 248376, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 22, 8, 54, 21, 248402, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 22, 8, 54, 21, 247350, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 22, 8, 54, 21, 247381, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
