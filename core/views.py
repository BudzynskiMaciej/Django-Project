from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate
from core.forms import UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView
from django.utils.translation import ugettext_lazy as _
from youtube.tasks import fetch_user_videos

# Create your views here.


class UserView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/detail.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            fetch_user_videos.delay(form.cleaned_data['username'])
            messages.success(request, _('Account created successfully'))
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            messages.warning(request, _('There are some problems with form.'))
    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})
