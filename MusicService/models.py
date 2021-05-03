from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return " ".join(( self.fname,self.lname))

class Audio(models.Model):
    audio_id = models.IntegerField()
    file_name = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.file_name