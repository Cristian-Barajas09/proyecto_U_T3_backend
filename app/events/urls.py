"""This module contains the urls for the events app."""
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

app_name = 'events' # pylint: disable=invalid-name

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')

urlpatterns = router.urls
