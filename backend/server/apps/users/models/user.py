from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='Никнейм'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}'

