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
            # 'get_post'
        ]

    def get_likes(self, obj):
        serializer = PostSerializer(obj.likes.all(), many=True)

        return serializer.data

    def get_comments(self, obj):
        serializer = CommentSerializer(obj.comments.all(), many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField('get_replies')
    me_liked = serializers.SerializerMethodField('get_me_liked')
    likes_count = serializers.SerializerMethodField('get_likes_count')

    class Meta:
        model = PostComment
        fields = [
            'id',
            'author',
            'comment',
            'parent',
            'published_time',
            'replies',
            'likes_count',
            'me_liked'
        ]

    def get_replies(self, obj):
        if obj.child.exists():
            serializers = self.__class__(
                obj.child.all(), many=True, context=self.context)
            return serializers.data
        else:
            return None

    def get_me_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(author=user).exists()
        else:
            return False

    def get_likes_count(self, obj):
        return obj.likes.count()


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
            'post']
