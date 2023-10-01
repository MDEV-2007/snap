from django.urls import path
from .views import *

urlpatterns = [
    path('add-like/', add_like),
    path('post-list/', PostListApiView.as_view()),
    path('post-create/', PostCreateApiView.as_view()),
    path('post-edit/', PostRetriveUpdateApiView.as_view()),
    path('post/<uuid:pk>/', PostCommentListView.as_view()),

    path('post-comment-create/', PostCommentCreateApiView.as_view()),
]
