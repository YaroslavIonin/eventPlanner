from django.db import models
from django_admin_geomap import GeoItem
from django.core.validators import MinValueValidator, MaxValueValidator


class Location(models.Model, GeoItem):
    owner = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='locations',
        verbose_name='Владелец',
        help_text='Создатель адреса',
    )
    address = models.CharField(
        max_length=55,
        verbose_name='Адрес',
    )
    latitude = models.FloatField(
        validators=(
            MinValueValidator(-90),
            MaxValueValidator(90),
        ),
        verbose_name='Широта',
    )
    longitude = models.FloatField(
        validators=(
            MinValueValidator(-180),
            MaxValueValidator(180),
        ),
        verbose_name='Долгота',
    )

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    def __str__(self):
        return self.address
