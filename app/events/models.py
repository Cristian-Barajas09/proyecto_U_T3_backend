from dataclasses import dataclass
from django.db import models
from django.utils import timezone

# Create your models here.
class EventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Event(models.Model):

    logic = EventManager()

    title = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    @dataclass
    class Meta:
        db_table = 'events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title', 'date']),
        ]