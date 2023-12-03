
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class SearchEntry(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    query = models.CharField(max_length=255)  
    age = models.PositiveIntegerField(null=True, blank=True, default=0)
    iq_level = models.PositiveIntegerField(null=True, blank=True, default=0)
    coding_level = models.PositiveIntegerField(null=True, blank=True, default=0)
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.user.username} Search Entry"

