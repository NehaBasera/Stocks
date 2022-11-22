import profile

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db import transaction
from django.shortcuts import render, redirect
from moneymarket import models
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from .models import Profile, User
from .models import User
from django.contrib.auth import login, authenticate
from django.conf import settings
from .forms import SignupForm, ProfileForm
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pwd)
            login(request, user)
            return redirect('index')
        else:
            note = form.errors
            return render(request, 'registration/signup.html', {'note': note})
    else:
        form = SignupForm
        profile_form = ProfileForm()
        note = form.errors
        return render(request, 'registration/signup.html', {'form': form, 'note': note, 'profile_form': profile_form})











@login_required
def profile(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('edit_profile')

    else:
        user_form = SignupForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context= {
                'user_form' : user_form,
                'profile_form' : profile_form
        }

    return render(request,'registration/edit_profile.html', context)