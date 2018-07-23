from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Video
from .services import YoutubeService
from DjangoTut.settings import YOUTUBE_API_ACCESS_KEY as API_KEY
from core.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


class PopularVideosList(ListView):
    YoutubeService.get_most_popular_videos(15, 'PL', API_KEY)
    template_name = 'index.html'
    context_object_name = 'most_popular_videos'

    def get_queryset(self):
        return Video.objects.filter(is_most_viewed=True)


class PopularVideosDetail(DetailView):
    model = Video
    template_name = 'youtube/popularVideosDetail.html'


@login_required
def my_videos_list_view(request):
    user = request.user.username
    YoutubeService.get_my_videos(user, API_KEY)
    my_videos_list = Video.objects.filter(
            channel_id__exact=YoutubeService.get_user_channel_id(user, API_KEY)
        ).order_by('-published_at')[:15]
    context = {'my_videos': my_videos_list}
    return render(request, 'youtube/myVideosList.html', context)
