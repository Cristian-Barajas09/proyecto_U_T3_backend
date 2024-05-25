from rest_framework import routers
from .api import PlatesViewset, CategoryViewset, IngredientViewset

route = routers.DefaultRouter()

route.register('plates', PlatesViewset , 'plates')
route.register('categories', CategoryViewset , 'category')
route.register('ingredients', IngredientViewset , 'ingredient')

urlpatterns = route.urls


