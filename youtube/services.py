import requests
from .models import Video
from core.utils import db_table_exists
from django.utils import timezone
from core.models import User


class YoutubeService:

    @staticmethod
    def get_user_channel_id(username, api_key):
        r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=id&forUsername=' + username
                         + '&key=' + api_key)
        r = r.json()
        if not r['items']:
            return None
        return r['items'][0]['id']

    @staticmethod
    def get_my_videos(username, api_key, max_results=15):
        if not(db_table_exists('youtube_video')):
            return None
        my_videos = []
        if not User.is_authenticated:
            return None
        r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=' +
                         username + '&key=' + api_key)
        r = r.json()
        if not r['items']:
            return None
        my_uploaded_playlist = r['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        r = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=' +
                         str(max_results) + '&playlistId=' + my_uploaded_playlist + '&key=' + api_key)
        r = r.json()
        for item in r['items']:
            youtube_id = item['snippet']['resourceId']['videoId']
            published_at = item['snippet']['publishedAt']
            channel_id = item['snippet']['channelId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail = item['snippet']['thumbnails']['medium']['url']
            channel_title = item['snippet']['channelTitle']
            if Video.objects.filter(youtube_id=youtube_id, title=title).exists():
                continue
            video = Video.objects.create(youtube_id=youtube_id, published_at=published_at, channel_id=channel_id,
                                         title=title, description=description, thumbnail=thumbnail,
                                         channel_title=channel_title)
            my_videos.append(video)
        return my_videos
        pass

    @staticmethod
    def get_most_popular_videos(max_results, region_code, api_key):
        if not(db_table_exists('youtube_video')):
            return None
        most_popular_videos = []
        r = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet%2Cstatistics&chart=mostPopular&maxResults='
                         + str(max_results) + '&regionCode=' + region_code + '&key=' + api_key)
        r = r.json()
        if Video.objects.all().exists():
            for video in Video.objects.all():
                if video.expiration_date == timezone.now():
                    video.delete()
        for item in r['items']:
            youtube_id = item['id']
            published_at = item['snippet']['publishedAt']
            channel_id = item['snippet']['channelId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail = item['snippet']['thumbnails']['medium']['url']
            channel_title = item['snippet']['channelTitle']
            view_count = item['statistics']['viewCount']
            like_count = item['statistics']['likeCount']
            dislike_count = item['statistics']['dislikeCount']
            comment_count = item['statistics']['commentCount']
            if Video.objects.filter(youtube_id=youtube_id, title=title).exists():
                continue
            video = Video.objects.create(youtube_id=youtube_id, published_at=published_at, channel_id=channel_id,
                                         title=title, description=description, thumbnail=thumbnail,
                                         channel_title=channel_title, view_count=view_count, like_count=like_count,
                                         dislike_count=dislike_count, comment_count=comment_count, is_most_viewed=True)
            most_popular_videos.append(video)
        return most_popular_videos
