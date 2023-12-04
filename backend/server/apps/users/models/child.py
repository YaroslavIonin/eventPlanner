from django.db import models


class Child(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='Имя'
    )
    parent = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родитель',
    )

    class Meta:
        verbose_name = 'Ребёнок'
        verbose_name_plural = 'Дети'

    def __str__(self) -> str:
        return f'{self.name}'
