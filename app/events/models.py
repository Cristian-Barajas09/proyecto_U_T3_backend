"""Events models"""
from dataclasses import dataclass
from django.db import models
from django.utils import timezone

# Create your models here.
class EventManager(models.Manager):
    """Custom manager for Event model"""
    def get_queryset(self):
        """Get all objects that are not deleted"""
        return super().get_queryset().filter(deleted_at__isnull=True)

class EventAllManager(models.Manager):
    """All objects"""
    def get_queryset(self):
        return super().get_queryset()

class Event(models.Model):
    """Event model"""
    logic = EventManager()
    objects = EventAllManager()

    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restore the object from trash"""
        self.deleted_at = None
        self.save()
    @dataclass
    class Meta:
        """Meta class"""
        db_table = 'events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title', 'date']),
        ]
