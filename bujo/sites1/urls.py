from django.urls import path

from . import views



urlpatterns = [
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('key', views.key, name='key'),
    path('thisweek', views.thisweek, name='thisweek'),
    path('today', views.today, name='today'),
]