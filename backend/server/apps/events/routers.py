from rest_framework.routers import DefaultRouter

from .viewsets import EventViewSet

events_router = DefaultRouter()

events_router.register(
    prefix='events',
    viewset=EventViewSet,
    basename='events',
)
