from django.db import models
from django.contrib.auth.models import User
from dataclasses import dataclass


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @dataclass
    class Meta:
        db_table = 'Profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
# Create your models here.