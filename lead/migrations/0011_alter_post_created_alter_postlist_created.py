# Generated by Django 4.1.7 on 2023-04-16 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0010_alter_post_created_alter_postlist_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 5, 7, 38, 140548, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 5, 7, 38, 141137, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
