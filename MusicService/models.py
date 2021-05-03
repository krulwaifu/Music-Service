from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

# Create your models here.
class Audio(models.Model):
    file_name = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.file_name