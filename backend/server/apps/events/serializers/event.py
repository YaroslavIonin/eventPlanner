from rest_framework import serializers

from .location import LocationSerializer
from ..models import Event
from apps.users.serializers import (
    ChildSerializer,
    UserSummarySerializer,
)


class EventSerializer(serializers.ModelSerializer):
    child = ChildSerializer()
    location = LocationSerializer()
    owner = UserSummarySerializer()

    class Meta:
        model = Event
        fields = ('__all__')
