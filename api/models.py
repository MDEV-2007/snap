from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', default='../static/images/default.jpg')

    def __str__(self):
        return self.username



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fallowing_account')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower.username + "->" + self.following.username

    class Meta:
        ordering = ['created']

    