from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(
        blank=True, null=True, upload_to=f'users/profile_photo/', verbose_name='Profile picture')

    class Meta:
        ordering = ['date_joined']
