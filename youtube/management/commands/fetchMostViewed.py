from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from youtube.services import YoutubeService
from youtube.models import Video
from core.utils import db_table_exists


class Command(BaseCommand):
    help = 'Get MostViewed Videos from Youtube and adds them to database'

    def add_arguments(self, parser):
        parser.add_argument('regionCode', type=str, default='PL')

    def handle(self, *args, **options):
        if not(db_table_exists('youtube_video')):
            raise CommandError('There are no youtube_video table in database, migrate first!')
        youtube = YoutubeService()
        most_viewed_videos_to_add = youtube.get_most_popular_videos(15, options['regionCode'])
        Video.objects.filter(expiration_date__lte=timezone.now()).update(is_most_viewed=False)
        current_most_viewed = Video.objects.filter(is_most_viewed=True)
        most_viewed_videos = [elem for elem in most_viewed_videos_to_add if elem not in current_most_viewed]
        Video.objects.bulk_create(most_viewed_videos)
        self.stdout.write(self.style.SUCCESS('Successfully added Most Viewed Videos to database!'))
