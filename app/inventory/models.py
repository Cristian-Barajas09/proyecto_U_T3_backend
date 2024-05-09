from django.db import models

class Plates(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.URLField()
    price = models.DecimalField(max_digits=5,max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
