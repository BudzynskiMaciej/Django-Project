from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from youtube.services import YoutubeService
from youtube.models import Video
from core.utils import db_table_exists


class Command(BaseCommand):
    help = 'Get MostViewed Videos from Youtube and adds them to database'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, default='Google')

    def handle(self, *args, **options):
        if not(db_table_exists('youtube_video')):
            raise CommandError('There are no youtube_video table in database, migrate first!')
        youtube = YoutubeService()
        my_videos = youtube.get_my_videos(options['username'])
        if not my_videos:
            raise CommandError('No Videos for that username!')
        Video.objects.filter(expiration_date__lte=timezone.now()).delete()
        Video.objects.bulk_create(my_videos)
        self.stdout.write(self.style.SUCCESS('Successfully added Your Videos to database!'))
