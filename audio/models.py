from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

# Create your models here.
class Audio(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()