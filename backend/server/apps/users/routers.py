from rest_framework.routers import DefaultRouter

from .views import ChildViewSet

children_router = DefaultRouter()

children_router.register(
    prefix='children',
    viewset=ChildViewSet,
    basename='children',
)
