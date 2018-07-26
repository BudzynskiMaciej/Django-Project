import requests
from .models import Video
from DjangoTut.settings import YOUTUBE_API_ACCESS_KEY


class YoutubeService:
    API_KEY = None
    METHOD_GET = 'get'
    METHOD_POST = 'post'
    METHOD_DELETE = 'delete'

    def __init__(self):
        self.BASE_API_URL = "https://www.googleapis.com/youtube/v3/"

        self.api_key = YOUTUBE_API_ACCESS_KEY
        if self.api_key is None:
            print("Error Reading API_KEY, Service will not work")

    def _make_request(self, resource, params, method='get'):
        url = self.BASE_API_URL + resource
        if method == YoutubeService.METHOD_GET:
            request = requests.get(url, params)
        elif method == YoutubeService.METHOD_POST:
            request = requests.post(url, params)
        elif method == YoutubeService.METHOD_DELETE:
            request = requests.delete(url)
        return request.json()

    def get_my_videos(self, username, max_results=15):
        my_videos = []
        params = {
            'part': 'contentDetails',
            'forUsername': username,
            'key': self.api_key,
        }
        request = self._make_request('channels', params)
        if not request['items']:
            return my_videos
        my_uploaded_playlist = request['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        params = {
            'part': 'snippet',
            'maxResults': str(max_results),
            'playlistId': my_uploaded_playlist,
            'key': self.api_key,
        }
        request = self._make_request('playlistItems', params)
        for item in request['items']:
            youtube_id = item['snippet']['resourceId']['videoId']
            published_at = item['snippet']['publishedAt']
            channel_id = item['snippet']['channelId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail = item['snippet']['thumbnails']['medium']['url']
            channel_title = item['snippet']['channelTitle']
            video = Video(youtube_id=youtube_id, published_at=published_at, channel_id=channel_id, title=title,
                          description=description, thumbnail=thumbnail, channel_title=channel_title)
            my_videos.append(video)
        return my_videos

    def get_most_popular_videos(self, max_results, region_code):
        most_popular_videos = []
        params = {
            'part': 'snippet,statistics',
            'chart': 'mostPopular',
            'maxResults': str(max_results),
            'regionCode': region_code,
            'key': self.api_key
        }
        request = self._make_request('videos', params)
        for item in request['items']:
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
            if 'commentCount' not in item['statistics']:
                comment_count = 0
            else:
                comment_count = item['statistics']['commentCount']
            video = Video(youtube_id=youtube_id, published_at=published_at, channel_id=channel_id, title=title,
                          description=description, thumbnail=thumbnail, channel_title=channel_title,
                          view_count=view_count, like_count=like_count, dislike_count=dislike_count,
                          comment_count=comment_count, is_most_viewed=True)
            most_popular_videos.append(video)
        return most_popular_videos
