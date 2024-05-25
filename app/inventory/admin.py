from django.contrib import admin
from .models import Plates,Category,Ingredient
# Register your models here.

admin.site.register(Plates)
admin.site.register(Category)
admin.site.register(Ingredient)