from typing import Type

from rest_framework import mixins, viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from apps.users.models import Child
from ..serializers import ChildSerializer


class ChildViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    SERIALIZER_CLASS_MAP = {
        'list': ChildSerializer,
        'create': ChildSerializer,
    }

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        return self.SERIALIZER_CLASS_MAP.get(self.action, ChildSerializer)

    def get_queryset(self):
        queryset = Child.objects.filter(
            parent=self.request.user,
        )
        return queryset
