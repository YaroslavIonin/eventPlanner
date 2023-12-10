from django.db import models


class Schedule(models.Model):
    name = models.CharField(
        max_length=55,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return self.name


class DaySchedule(models.Model):
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 1, 'пн'
        TUESDAY = 2, 'вт'
        WEDNESDAY = 3, 'ср'
        THURSDAY = 4, 'чт'
        FRIDAY = 5, 'пт'
        SATURDAY = 6, 'сб'
        SUNDAY = 7, 'вс'

    day_of_week = models.IntegerField(
        choices=DayOfWeek.choices,
        default=DayOfWeek.MONDAY,
        verbose_name='День недели'
    )
    time_start = models.TimeField(
        verbose_name='Начало в',
    )
    time_finish = models.TimeField(
        verbose_name='Окончание в',
    )
    schedule = models.ForeignKey(
        to='events.Schedule',
        on_delete=models.CASCADE,
        related_name='days',
        verbose_name='Расписание',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'День расписания'
        verbose_name_plural = 'Дни расписания'

    def __str__(self):
        return f'{self.schedule.name} - {self.day_of_week}'
