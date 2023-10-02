from rest_framework import serializers
from .models import User


class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'verified']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(required=False)

    followers = serializers.SerializerMethodField('get_followers')
    following = serializers.SerializerMethodField('get_following')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email',
                  'avatar', 'followers', 'following', 'verified']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_followers(self, obj):
        return FollowerSerializer([x.follow for x in obj.following.all()], many=True).data

    def get_following(self, obj):
        return FollowerSerializer([x.user for x in obj.followers.all()], many=True).data
