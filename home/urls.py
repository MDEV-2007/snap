from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('explore/', explore, name='explore'),
    path('search/', search, name='search'),
    path('notifications/', notification, name='notification'),
    path('reels/', reels, name='reels'),
    path('create/', create, name='create'),
    path('messages/', message, name='messages'),
    path('profiles/', profile, name='profile'),
]