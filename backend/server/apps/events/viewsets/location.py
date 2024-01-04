from django.db.models import QuerySet

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.events.models import Location
from apps.events.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Location.objects.filter(
            owner=self.request.user,
        )
        return queryset
