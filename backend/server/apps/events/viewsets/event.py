from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, serializers, pagination, filters


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

