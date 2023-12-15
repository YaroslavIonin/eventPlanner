from django.contrib import admin

from ..models import Schedule, DaySchedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DaySchedule)
class DayScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'day_of_week')
