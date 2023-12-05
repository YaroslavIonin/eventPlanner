from django.urls import path, include

from ..routers import children_router
from ..views import UserSummaryAPIView


urlpatterns = [
    path('', include(children_router.urls)),
    path('me/', UserSummaryAPIView.as_view()),
]
