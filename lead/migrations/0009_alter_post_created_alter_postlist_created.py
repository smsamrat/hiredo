# Generated by Django 4.1.7 on 2023-04-16 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0008_postlist_response_count_alter_post_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 47, 5, 159802, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 16, 3, 47, 5, 160415, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
