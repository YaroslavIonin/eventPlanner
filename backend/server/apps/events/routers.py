from rest_framework.routers import DefaultRouter

from .viewsets import EventViewSet, LocationViewSet

events_router = DefaultRouter()

events_router.register(
    prefix='events',
    viewset=EventViewSet,
    basename='events',
)
events_router.register(
    prefix='locations',
    viewset=LocationViewSet,
    basename='locations',
)
