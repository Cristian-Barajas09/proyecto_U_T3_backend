"""Urls for sales app"""
from rest_framework import routers
from .views import OrderViewset, OrderPlatesViewset, PayMethodViewset, PaymentViewset

route = routers.DefaultRouter()

route.register('orders', OrderViewset , 'orders')

route.register ('order/plates', OrderPlatesViewset, 'OrderPlates')

route.register ('paymethods', PayMethodViewset, 'paymethods')

route.register ('payments', PaymentViewset, 'payments')

urlpatterns = route.urls
