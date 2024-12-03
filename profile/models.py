# profile/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    lastName = models.CharField(max_length=100, blank=True, null=True)
    nickName = models.CharField(max_length=100, blank=True, null=True)
    
