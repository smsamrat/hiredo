# Generated by Django 4.1.7 on 2023-04-18 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0021_alter_post_created_alter_postlist_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 18, 5, 19, 47, 552053, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 18, 5, 19, 47, 552718, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]