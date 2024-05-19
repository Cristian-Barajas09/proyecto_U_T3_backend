from rest_framework import routers
from .views import CurrencyViewset, CurrencyConverterViewset

route = routers.DefaultRouter()

route.register('Currencies', CurrencyViewset , 'Currencies')

route.register('CurrenciesConverter', CurrencyConverterViewset, 'CurrenciesConverter')

urlpatterns = route.urls


