from typing import Type
from django.utils import timezone

from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, serializers, filters, status
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Event
from ..filtersets import EventFilterSet
from ..serializers import (
    EventSerializer,
    CreateOneTimeEventSerializer,
    CreateEventWithScheduleSerializer,
)
from ..utils import create_with_schedule


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend,)
    filterset_class = EventFilterSet

    SERIALIZER_CLASS_MAP = {
        'list': EventSerializer,
        'create': CreateOneTimeEventSerializer,
        'create_with_schedule': CreateEventWithScheduleSerializer,
    }

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        return self.SERIALIZER_CLASS_MAP.get(self.action, EventSerializer)

    def get_queryset(self) -> QuerySet:
        queryset = Event.objects.filter(
            owner=self.request.user,
            # event_date__month=timezone.now().month,
            # event_date__year=timezone.now().year,
        ).order_by('event_date', 'event_time_start')
        return queryset

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer_class()
        response = serializer(queryset, many=True).data
        return Response(response)

    @action(methods=('POST',), detail=False, url_path='schedule')
    def create_with_schedule(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = create_with_schedule(serializer.data, user=request.user.id)
        return Response(status=status.HTTP_201_CREATED)

