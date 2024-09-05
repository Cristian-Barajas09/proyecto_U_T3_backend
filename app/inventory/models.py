"""Models for Inventory app"""
from django.db import models

class Plates(models.Model):
    """Model for Plates"""
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(null=True, blank=True,max_length=250)
    price = models.DecimalField(max_digits=5,max_length=10,decimal_places=2)
    categories = models.ManyToManyField('Category', related_name='plates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class CategoryManager(models.Manager):
    """Manager for Category"""
    def get_queryset(self) -> models.QuerySet:
        """Get queryset"""
        return super().get_queryset().filter(deleted_at__isnull=True)

class Category(models.Model):
    """Model for Category"""

    objects = models.Manager()
    active_objects = CategoryManager()


    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
