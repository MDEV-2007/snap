from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import *
from .serializers import *


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Post.objects.all()


class PostCreateApiView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]
    # pagination_class = [JSONParser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetriveUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def put(self, request, *args, **kwargs):
        post = self.get.objects()
        serializer = self.get_serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "code": status.HTTP_200_OK,
                "message": "Post successfully updates",
                'data': serializer.data
            }
        )

    def delete(self, request, *args, **kwargs):
        post = self.get.objects()
        post.delete()
        return Response(
            {
                "success": True,
                "code": status.HTTP_204_NO_CONTENT,
                "message": "Post successfully delete", }
        )


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        queryset = PostComment.objects.filter(post__id=post_id)
        return queryset
