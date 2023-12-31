from rest_framework import serializers

from ..constants import EventErrors
from ..models import Event, Location
from .location import LocationSerializer
from .schedule import ScheduleSerializer, ScheduleCreateSerializer

from apps.users.models import Child
from apps.users.serializers import (
    ChildSerializer,
    UserSummarySerializer,
)


class EventSerializer(serializers.ModelSerializer):
    child = ChildSerializer()
    location = LocationSerializer()
    owner = UserSummarySerializer()
    schedule = ScheduleSerializer()

    class Meta:
        model = Event
        fields = (
            'id',
            'child',
            'location',
            'owner',
            'main_name',
            'event_date',
            'event_time_start',
            'event_time_finish',
            'event_description',
            'schedule',
        )


class CreateOneTimeEventSerializer(serializers.ModelSerializer):
    child = serializers.PrimaryKeyRelatedField(
        queryset=Child.objects.all(),
        required=False,
    )
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        required=False,
    )

    class Meta:
        model = Event
        fields = (
            'main_name',
            'child',
            'event_date',
            'event_time_start',
            'event_time_finish',
            'event_description',
            'location',
        )

    def create(self, validated_data: dict) -> Event:
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def validate_child(self, child: Child) -> Child:
        user = self.context['request'].user

        if child not in user.children.all():
            raise serializers.ValidationError(EventErrors.NOT_USERS_CHILD)
        else:
            return child

    def validate_location(self, location: Location) -> Location:
        user = self.context['request'].user

        if location not in user.locations.all():
            raise serializers.ValidationError(EventErrors.NOT_USERS_LOCATION)
        else:
            return location

    @property
    def data(self):
        return EventSerializer(instance=self.instance).data


class CreateEventWithScheduleSerializer(serializers.ModelSerializer):
    child = serializers.PrimaryKeyRelatedField(
        queryset=Child.objects.all(),
        required=False,
    )
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        required=False,
    )
    schedule = ScheduleCreateSerializer()

    class Meta:
        model = Event
        fields = (
            'main_name',
            'child',
            'event_description',
            'location',
            'schedule',
        )

    def create(self, validated_data: dict) -> Event:
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def validate_child(self, child: Child) -> Child:
        user = self.context['request'].user

        if child not in user.children.all():
            raise serializers.ValidationError(EventErrors.NOT_USERS_CHILD)
        else:
            return child

    def validate_location(self, location: Location) -> Location:
        user = self.context['request'].user

        if location not in user.locations.all():
            raise serializers.ValidationError(EventErrors.NOT_USERS_LOCATION)
        else:
            return location
