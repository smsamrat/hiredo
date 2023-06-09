# Generated by Django 4.1.7 on 2023-05-05 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0009_alter_creditpurchasedbyuser_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 57, 34, 660844, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 57, 34, 660859, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 57, 34, 660215, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 5, 11, 57, 34, 660235, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
