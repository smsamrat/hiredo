# Generated by Django 4.1.7 on 2023-04-09 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 9, 10, 46, 51, 159083, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postlist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 9, 10, 46, 51, 159083, tzinfo=datetime.timezone.utc)),
        ),
    ]
