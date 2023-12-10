from rest_framework import serializers

from apps.events.models import Schedule, DaySchedule


class DayScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaySchedule
        fields = ('day_of_week', 'time_start', 'time_finish')


class ScheduleSerializer(serializers.ModelSerializer):
    days = DayScheduleSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('id', 'days',)
