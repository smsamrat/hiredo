# Generated by Django 4.1.7 on 2023-05-08 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0017_alter_creditpurchasedbyuser_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 8, 9, 42, 6, 784917, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="creditpurchasedbyuser",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 8, 9, 42, 6, 784934, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 8, 9, 42, 6, 784259, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="setcreditpurchased",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 8, 9, 42, 6, 784285, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
