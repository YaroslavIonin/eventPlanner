from django.db import models


class Event(models.Model):
    owner = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Владелец',
        help_text='Создатель события',
    )
    main_name = models.CharField(
        max_length=255,
        verbose_name='Название события',
        help_text='Название события',
    )
    event_date = models.DateField(
        verbose_name='Дата события',
        help_text='Дата события',
    )
    event_time = models.TimeField(
        verbose_name='Время события',
        help_text='Время события',
        blank=True,
        null=True,
    )
    location = models.ForeignKey(
        to='events.Location',
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Местоположение',
        blank=True,
        null=True,
    )
    event_description = models.TextField(
        max_length=5000,
        verbose_name='Описание заведения',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.main_name
