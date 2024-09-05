"""This file is used to define the urls for the inventory app."""
from rest_framework import routers
from inventory.api import PlatesViewset, CategoryViewset

route = routers.DefaultRouter()

route.register(r'plates', PlatesViewset , 'plates')
route.register(r'categories', CategoryViewset , 'categories')


urlpatterns = route.urls
