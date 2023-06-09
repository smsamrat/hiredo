# Generated by Django 4.1.7 on 2023-05-03 04:26

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lead", "0028_alter_post_created_alter_postlist_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postlist",
            name="not_interested_users",
            field=models.ManyToManyField(
                blank=True,
                related_name="not_interested_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 882930, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 883540, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknow",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 888303, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknowservice",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 3, 4, 26, 23, 887684, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
