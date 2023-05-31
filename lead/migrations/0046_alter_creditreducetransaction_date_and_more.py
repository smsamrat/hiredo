# Generated by Django 4.1.7 on 2023-05-23 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0045_alter_creditreducetransaction_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditreducetransaction",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 11, 27, 11, 591961, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 11, 27, 11, 297862, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 11, 27, 11, 298643, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknow",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 11, 27, 11, 492057, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknowservice",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 23, 11, 27, 11, 490788, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]