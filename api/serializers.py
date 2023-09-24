from rest_framework import serializers
from .models import User, Follow


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'avatar']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ['id', 'created', 'following', 'follower']
