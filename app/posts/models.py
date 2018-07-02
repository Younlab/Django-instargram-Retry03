from django.db import models

from config import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_images', blank=True)
    content = models.TextField(blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        # 1. related_name은 반대쪽(target)에서 이쪽(source)로의 연결을 만들어주는 Manager
        # 2. 자신이 like_users에 포함이 되는 Post Query Set Manager
        # 3. -> 내가 좋아요를 누른 Post 목록
        related_name='like_posts',
    )

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

