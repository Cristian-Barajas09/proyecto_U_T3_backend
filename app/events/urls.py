"""This module contains the urls for the events app."""
from django.urls import path
from .views import EventAPIView, EventTrashAPIView, EventOneAPIView, EventOneTrashAPIView

app_name = 'events'


urlpatterns = [
    path('events/', EventAPIView.as_view(), name='events'),
    path('events/<int:event_id>/', EventOneAPIView.as_view(), name='event'),
    path('events/trash/all',EventTrashAPIView.as_view(), name='events-trash'),
    path('events/trash/<int:event_id>/',EventOneTrashAPIView.as_view(), name='event-trash'),
]
