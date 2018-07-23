# Generated by Django 2.0.7 on 2018-07-23 07:42

import core.utils
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_id', models.CharField(max_length=128)),
                ('published_at', models.DateTimeField(verbose_name='published_at')),
                ('channel_id', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=2048)),
                ('thumbnail', models.URLField()),
                ('channel_title', models.CharField(max_length=64)),
                ('view_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('dislike_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateTimeField(default=core.utils.one_day_later_than_now)),
                ('is_most_viewed', models.BooleanField(default=False)),
            ],
        ),
    ]
