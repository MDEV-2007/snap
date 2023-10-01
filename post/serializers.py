from rest_framework import serializers
from .models import Post, PostLike, PostComment, CommentLike
from api.models import User
from api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField('get_likes')
    comments = serializers.SerializerMethodField('get_comments')
    image_size = serializers.SerializerMethodField('get_image_size')

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
            'image_size',
        ]

    def get_likes(self, obj):
        serializer = PostLikeSerializer(obj.likes.all(), many=True)

        return serializer.data

    def get_comments(self, obj):
        serializer = CommentSerializer(obj.comments.all(), many=True)
        return serializer.data

    def get_image_size(self, obj: Post):
        return {
            'width': obj.image.width,
            'height': obj.image.height
        }


class CommentSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    post_id = serializers.UUIDField()
    parent = serializers.ReadOnlyField()

    class Meta:
        model = PostComment
        fields = [
            'id',
            'post_id',
            'author',
            'comment',
            'parent',
            'published_time',
        ]

    def validate(self, attrs):
        try:
            post_id = attrs.get('post_id')
            post = Post.objects.get(id=post_id)
            attrs['post'] = post
        except Post.DoesNotExist:
            raise serializers.ValidationError('Post does not exist')

        return super().validate(attrs)


class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = [
            'id',
            'author',
            'comment'
        ]


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
