from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('test_token/', views.test_token),
    path('check-user/', views.check_user),
]


