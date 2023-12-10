from django.urls import path, include

from ..routers import children_router
from ..views import UserProfilePIView


urlpatterns = [
    path('', include(children_router.urls)),
    path('profile/', UserProfilePIView.as_view()),
]
