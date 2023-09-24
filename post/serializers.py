from rest_framework import serializers
from .models import Post, PostLike, PostComment, CommentLike
from api.models import User
from api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField('get_likes')
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'image',
            'caption',
            'published_time',
            'comments',
            'likes',
        ]

    def get_likes(self, obj):
        serializer = PostLikeSerializer(obj.likes.all(), many=True)

        return serializer.data

    def get_comments(self, obj):
        serializer = CommentSerializer(obj.comments.all(), many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = [
            'id',
            'author',
            'comment',
            'parent',
            'published_time',
        ]

class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = [
            'id',
            'author',
            'comment']


class PostLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = [
            'id',
            'author',
            'post'
        ]
