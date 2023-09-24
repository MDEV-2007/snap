from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', default='../static/images/default.jpg')

    def __str__(self):
        return self.username

    