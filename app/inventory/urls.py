from rest_framework import routers
from .api import PlatesViewset, CategoryViewset

route = routers.DefaultRouter()

route.register(r'plates', PlatesViewset , 'plates')
route.register(r'categories', CategoryViewset , 'category')


urlpatterns = route.urls


