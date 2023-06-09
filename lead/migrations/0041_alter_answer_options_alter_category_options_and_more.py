# Generated by Django 4.1.7 on 2023-05-10 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0040_alter_creditreducetransaction_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer",
            options={"ordering": ["-id"], "verbose_name_plural": "Answers"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["-id"], "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="creditreducetransaction",
            options={
                "ordering": ["-id"],
                "verbose_name_plural": "Credit Reduce Transactions",
            },
        ),
        migrations.AlterModelOptions(
            name="location",
            options={"ordering": ["-id"], "verbose_name_plural": "Locations"},
        ),
        migrations.AlterModelOptions(
            name="myresponse",
            options={"ordering": ["-id"], "verbose_name_plural": "My Responses"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-id"], "verbose_name_plural": "Posts"},
        ),
        migrations.AlterModelOptions(
            name="postlist",
            options={"ordering": ["-id"], "verbose_name_plural": "Post Lists"},
        ),
        migrations.AlterModelOptions(
            name="postrequestlist",
            options={"ordering": ["-id"], "verbose_name_plural": "Post Request Lists"},
        ),
        migrations.AlterModelOptions(
            name="questions",
            options={"ordering": ["-id"], "verbose_name_plural": "Questions"},
        ),
        migrations.AlterModelOptions(
            name="realtimebooknow",
            options={"ordering": ["-id"], "verbose_name_plural": "RealTime Book Now"},
        ),
        migrations.AlterModelOptions(
            name="realtimebooknowservice",
            options={
                "ordering": ["-id"],
                "verbose_name_plural": "RealTime Book Now Services",
            },
        ),
        migrations.AlterModelOptions(
            name="recieveremailtemplate",
            options={
                "ordering": ["-id"],
                "verbose_name_plural": "Reciever Email Templates",
            },
        ),
        migrations.AlterModelOptions(
            name="wishlistfeatureservice",
            options={
                "ordering": ["-id"],
                "verbose_name_plural": "Wishlist Feature Services",
            },
        ),
        migrations.AlterModelOptions(
            name="wishlistprofileservice",
            options={
                "ordering": ["-id"],
                "verbose_name_plural": "Wishlist Profile Services",
            },
        ),
        migrations.AlterField(
            model_name="creditreducetransaction",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 997264, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 990515, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="postlist",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 991155, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknow",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 996149, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="realtimebooknowservice",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 21, 14, 995586, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
