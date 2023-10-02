from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatar/', default='../static/images/default.jpg')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    follow = models.ForeignKey(
        User, related_name='follower', on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.follow} => {self.user}'

    # @staticmethod
    # def unfollow(from_user, to_user):
    #     f = Follow.objects.filter(follower=from_user, followed=to_user).all()
    #     if f:
    #         f.delete()

    # @staticmethod
    # def user_followed(from_user):
    #     followeders = Follow.objects.filter(follower=from_user).all()
    #     user_followed = []
    #     for followeder in followeders:
    #         user_followed.append(followeder.followed)
    #     return user_followed
