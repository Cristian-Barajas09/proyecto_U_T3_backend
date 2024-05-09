from django.contrib import admin
from .models import Event
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title', 'date')
    list_filter = ('date', 'created_at')
    date_hierarchy = 'date'
    ordering = ('-date', '-created_at')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description', 'date')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        })
    )