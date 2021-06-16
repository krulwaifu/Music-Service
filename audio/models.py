from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

# Create your models here.
GENRE_CHOICE = [
    ('podcast', 'Podcast'),
    ('audioBook', 'AudioBook'),
    ('music', 'Music'),
]
class Audio(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(choices=GENRE_CHOICE,max_length=100)
    file = models.FileField()
    image = models.FileField()

class Transcription(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    text = models.TextField()

class Liked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
