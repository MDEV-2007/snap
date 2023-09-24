import uuid
from django.db.models import UniqueConstraint
from django.db import models
from django.core.validators import FileExtensionValidator, MaxLengthValidator
from api.models import User


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_image', validators=[
                              FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    caption = models.TextField(validators=[MaxLengthValidator(2000)])
    published_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class PostComment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child',
        null=True,
        blank=True

    )
    published_time = models.DateField(auto_now_add=True)


class PostLike(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    published_time = models.DateField(auto_now_add=True)

    contraints = [
        models.UniqueConstraint(
            fields=["author", "post"],
            name="my_constraint",
        )
    ]


class CommentLike(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        PostComment, on_delete=models.CASCADE, related_name='likes')
    published_time = models.DateField(auto_now_add=True)

    contraints = [
        models.UniqueConstraint(
            fields=["author", "post"],
            name="my_constraint",
        )
    ]

