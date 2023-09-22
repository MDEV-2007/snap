from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .serializers import *


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny],

    def get_queryset(self):
        return Post.objects.all()

