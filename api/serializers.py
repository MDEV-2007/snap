from rest_framework import serializers
<<<<<<< HEAD
from .models import User, Follow
=======
from .models import User
>>>>>>> a234a2f (murodulla)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'avatar']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


<<<<<<< HEAD
class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ['id', 'created', 'following', 'follower']
=======


>>>>>>> a234a2f (murodulla)
