from django.db import models
from django.contrib.auth.models import User
from inventory.models import Plates
from django.utils import timezone
from dataclasses import dataclass


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    plates_id = models.ForeignKey(Plates, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField()
    total = models.DecimalField(max_digits=12,decimal_places=2)

    @dataclass
    class Meta:
        db_table = 'Orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
# Create your models here.

class OrderPlates(models.Model):
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    plates_id= models.ForeignKey(Plates, on_delete=models.CASCADE)

class PayMethod(models.Model):

    currency= models.CharField(max_length=5)
    method= models.CharField(max_length=60)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.currency+" "+self.method

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    @dataclass
    class Meta:
        db_table = 'PayMethod'
        verbose_name = 'Paymethod'
        verbose_name_plural = 'Paymethods'

class Payment(models.Model):
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    method_id= models.ForeignKey(PayMethod, on_delete=models.CASCADE)
    