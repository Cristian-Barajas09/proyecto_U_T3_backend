from django.db import models
from django.contrib.auth.models import User
from inventory.models import Plates

class Order(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    plates_id=models.ForeignKey(Plates, on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    description=models.TextField()
    total= models.DecimalField(max_digits=12,decimal_places=2)
# Create your models here.

class OrderPlates(models.Model):
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    plates_id= models.ForeignKey(Plates, on_delete=models.CASCADE)

class PayMethod(models.Model):
    currency= models.CharField(max_length=5)
    method= models.CharField(max_length=60)

class Payment(models.Model):
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    method_id= models.ForeignKey(PayMethod, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True, blank=True)