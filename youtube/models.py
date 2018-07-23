from django.db import models
from django.utils import timezone
from core.utils import one_day_later_than_now

# Create your models here.


class Video(models.Model):
    youtube_id = models.CharField(max_length=128)
    published_at = models.DateTimeField('published_at')
    channel_id = models.CharField(max_length=128)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    thumbnail = models.URLField()
    channel_title = models.CharField(max_length=64)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=one_day_later_than_now)
    is_most_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.channel_title + " - " + self.title
