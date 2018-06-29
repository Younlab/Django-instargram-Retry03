from django.db import models

from config import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_images', blank=True)
    content = models.TextField(blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ['-pk']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Mata:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.content}'

