from django.urls import path, include

from ..routers import children_router
from ..views import UserProfileAPIView


urlpatterns = [
    path('', include(children_router.urls)),
    path('profile/', UserProfileAPIView.as_view()),
]
