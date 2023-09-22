from django.urls import path
from .views import *

urlpatterns = [
    path('post-list/', PostListApiView.as_view())
]