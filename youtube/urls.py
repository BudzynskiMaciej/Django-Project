from django.urls import path
from . import views


app_name = 'youtube'
urlpatterns = [
    path('<int:pk>/', views.PopularVideosDetail.as_view(), name='detail'),
    path('myvideos/', views.my_videos_list_view, name='myvideoslist')
]
