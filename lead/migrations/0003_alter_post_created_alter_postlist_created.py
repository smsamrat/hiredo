# Generated by Django 4.1.7 on 2023-04-11 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0002_alter_post_created_alter_postlist_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 11, 6, 53, 41, 404237, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 11, 6, 53, 41, 404975, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
