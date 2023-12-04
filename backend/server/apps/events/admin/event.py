from django.contrib import admin

from ..models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('main_name', 'owner', 'event_date')
    fieldsets = [
        (
            "Основная информация",
            {
                "fields": [('main_name', 'owner',), 'event_description']

            }

        ),
        (
            "Дата и время",
            {
                "fields": ['event_date', 'event_time']
            }
        ),
        (
            None,
            {
                "fields": ['location']
            }
        ),
    ]
