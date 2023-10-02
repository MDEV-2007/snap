from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('check-username/', views.check_user),
    path('get-me/', views.get_me),
    path('get-user/', views.get_user),
    path('follow/', views.follow),
]
