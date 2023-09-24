from rest_framework import serializers
from .models import Post, PostLike, PostComment, CommentLike
from api.models import User
from api.serializers import UserSerializer


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')

class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author = UserSerializer(read_only=True)
    post_likes_count = serializers.SerializerMethodField('get_post_likes_count')
    post_comments_count = serializers.SerializerMethodField('get_post_comments_count')

    class Meta:
        model = Post
        fields = [
            'id', 
            'author', 
            'image', 
            'caption', 
            'published_time',
            'post_comments_count',
            'post_likes_count',
            'get_post'
            ]

    def get_post_likes_count(self,obj):
        return obj.likes.count()

    def get_post_comments_count(self,obj):
        return obj.comments.count()




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
            
            ]

    def get_replies(self,obj):
        if obj.child.exists():
            serializers = self.__class__(obj.child.all(), many=True, context=self.context)
            return serializers.data
        else:
            return None
        
    def get_me_liked(self,obj):
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


