# Generated by Django 4.1.7 on 2023-05-07 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0037_alter_creditreducetransaction_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditreducetransaction",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 57, 381696, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 57, 374982, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 57, 375619, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknow",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 57, 380350, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknowservice",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 9, 33, 57, 379770, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]