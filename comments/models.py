from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile


# Create your models here.
class Comment(models.Model):
    """
    Comment model, related to post and user
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
