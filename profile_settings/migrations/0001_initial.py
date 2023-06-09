# Generated by Django 4.1.7 on 2023-04-09 10:47

import ckeditor.fields
import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('long_description', ckeditor.fields.RichTextField(default=None)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 4, 9, 10, 47, 12, 22663, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Badges',
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.CreateModel(
            name='HelpTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='StillNeedHelp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Still Need Help',
            },
        ),
        migrations.CreateModel(
            name='Social_Media_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=100, null=True)),
                ('twitter', models.URLField(blank=True, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, max_length=100, null=True)),
                ('linkdin', models.URLField(blank=True, max_length=100, null=True)),
                ('websit_link', models.URLField(blank=True, max_length=100, null=True)),
                ('created_at', models.URLField(blank=True, max_length=100, null=True)),
                ('updated_at', models.URLField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Social_Media_Link',
                'verbose_name_plural': 'Social_Media_Links',
            },
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('comment', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 4, 9, 10, 47, 12, 22663, tzinfo=datetime.timezone.utc))),
                ('reviewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_given', to=settings.AUTH_USER_MODEL)),
                ('reviewed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ReviewRating',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=' ', upload_to='profile')),
                ('credit', models.IntegerField(blank=True, default=0, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('badges', models.ManyToManyField(blank=True, null=True, to='profile_settings.badge')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
                'db_table': 'Profile',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_settings.helptopic')),
            ],
            options={
                'verbose_name_plural': 'Helps',
            },
        ),
        migrations.CreateModel(
            name='Elit_Pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_views', models.CharField(blank=True, max_length=100, null=True)),
                ('total_massege_and_response', models.CharField(blank=True, max_length=100, null=True)),
                ('total_search', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Elit_Pro',
                'verbose_name_plural': 'Elit_Pro',
            },
        ),
        migrations.CreateModel(
            name='Account_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_email', models.CharField(blank=True, max_length=100, null=True)),
                ('usage_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('sms_notification_number', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account_Details',
                'verbose_name_plural': 'Account_Details',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logo')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='company_logo')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('websit_link', models.URLField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('company_siz', models.CharField(blank=True, max_length=100, null=True)),
                ('years_of_business', models.CharField(blank=True, max_length=100, null=True)),
                ('discription', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
    ]
