"""URLs for the API app."""
from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('example/', views.ExampleView.as_view(), name='example-view'),
    path('',include('events.urls')),
]
