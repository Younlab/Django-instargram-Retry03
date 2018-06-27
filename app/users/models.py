from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CHOICES_GENDER = (
        ('m', '남성'),
        ('f', '여자'),
        ('x', '당신이 괜찮다면 설정해주세요.'),
    )
    profile_image = models.ImageField(upload_to='profile_image', blank=True ,help_text='사진을 넣어주세요',)
    site_url = models.URLField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)

    def __str__(self):
        return self.username