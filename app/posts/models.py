from django.db import models

from config import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_images', blank=True)
    content = models.TextField(blank=True)
    created_at = models.TimeField(auto_now_add=True,auto_now=False)

