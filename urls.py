from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('edit_profile/', views.profile, name='edit_profile'),
    path('accounts/signup',views.signup,name='signup'),


]