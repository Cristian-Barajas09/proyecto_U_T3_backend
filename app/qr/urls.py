from django.urls import path

from . import views

urlpatterns = [
    path('qr/', views.qr_view, name='generate_qr'),

]
