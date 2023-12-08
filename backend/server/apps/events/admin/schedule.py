from django.contrib import admin

from ..models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'time_start', 'time_finish', 'event',)
    fieldsets = [
        (
            "Основная информация",
            {
                "fields": ['day_of_week', ('time_start', 'time_finish')]

            }

        ),
        (
            'Событие',
            {
                "fields": ['event']
            }
        ),
    ]
