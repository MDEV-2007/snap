from rest_framework import serializers
from .models import User


class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'verified']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(required=False)

    follower = serializers.SerializerMethodField('get_follower')
    following = serializers.SerializerMethodField('get_following')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email',
                  'avatar', 'follower', 'following', 'verified']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_follower(self, obj):
        # print(obj.username)
        # print(obj.follower.all())

        return FollowerSerializer([x.user for x in obj.follower.all()], many=True).data

    def get_following(self, obj):
        # print(obj.following)

        return FollowerSerializer([x.follow for x in obj.following.all()], many=True).data
