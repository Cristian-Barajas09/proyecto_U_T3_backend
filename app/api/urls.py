"""URLs for the API app."""
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewset, basename='profiles')

app_name = 'api'

urlpatterns = [
    path('example/', views.ExampleView.as_view(), name='example-view'),
    path('',include('events.urls')),
    path('',include('inventory.urls')),
    path ('',include('sales.urls')),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.UserView.as_view(), name='create_user'),
]


