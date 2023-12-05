from django.urls import path, include

from apps.events.routers import events_router

urlpatterns = [
    path('auth/', include('apps.users.urls.auth')),
    path('users/', include('apps.users.urls.user_urls')),
] + events_router.urls
