from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment_text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='profiles')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='profiles')

    def __str__(self):
        return self.user



