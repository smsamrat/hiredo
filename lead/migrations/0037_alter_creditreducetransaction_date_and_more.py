# Generated by Django 4.1.7 on 2023-05-07 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0036_alter_creditreducetransaction_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditreducetransaction",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 27, 179840, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 27, 172836, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 27, 173446, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknow",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 27, 178566, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknowservice",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 27, 177953, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
