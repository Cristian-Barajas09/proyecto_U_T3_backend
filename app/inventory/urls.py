from rest_framework import routers
from .api import PlatesViewset

route = routers.DefaultRouter()

route.register('plates', PlatesViewset , 'plates')

urlpatterns = route.urls


