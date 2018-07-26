from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


class PopularVideosList(ListView):
    template_name = 'index.html'
    context_object_name = 'most_popular_videos'

    def get_queryset(self):
        return Video.objects.filter(is_most_viewed=True)


class PopularVideosDetail(DetailView):
    model = Video
    template_name = 'youtube/popularVideosDetail.html'


class MyVideosList(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.username
        my_videos_list = Video.objects.filter(
            channel_title__exact=user
        ).order_by('-published_at')[:15]
        context = {'my_videos': my_videos_list}
        return render(request, 'youtube/myVideosList.html', context)
