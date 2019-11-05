from django.db import models
from django.contrib.auth.models import AbstractUser


class MainUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def is_user(self, user):
        return self.id == user.id


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'MainUser'
        verbose_name_plural = 'MainUsers'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
