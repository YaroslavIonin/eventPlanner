from rest_framework import serializers

from apps.events.constants import EventErrors
from apps.events.models import Schedule, DaySchedule


class DayScheduleSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['time_finish'] < data['time_start']:
            raise serializers.ValidationError(EventErrors.FINISH_TIME_BEFORE_START_TIME)
        return data

    class Meta:
        model = DaySchedule
        fields = ('day_of_week', 'time_start', 'time_finish')


class ScheduleSerializer(serializers.ModelSerializer):
    days = DayScheduleSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('id', 'days',)


class ScheduleCreateSerializer(serializers.ModelSerializer):
    days = DayScheduleSerializer(many=True)

    class Meta:
        model = Schedule
        fields = (
            'days',
            'date_start',
            'date_finish',
        )
