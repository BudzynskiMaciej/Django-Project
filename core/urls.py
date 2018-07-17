from django.urls import path, include
from django.views.generic.base import TemplateView
from core.views import UserView, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('accounts/<int:pk>/', UserView.as_view(), name='user_view'),
    path('secret/', TemplateView.as_view(template_name='accounts/secret.html'), name='secret'),
]