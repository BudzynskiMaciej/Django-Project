# Create your tasks here
from __future__ import absolute_import, unicode_literals
import celery
from django.core import management


@celery.task
def cleanup():
    try:
        management.call_command("fetchMostViewed", 'PL')
        return "success"
    except Exception as e:
        print(e)

@celery.task
def fetch_user_videos(username):
    try:
        management.call_command("fetchMyVideos", str(username))
        return "success"
    except Exception as e:
        print(e)
