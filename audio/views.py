from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from icecream import ic
from MusicService.models import Audio

def get_audio(request,fname):
    global response
    if request.method == "GET":
        try:
            audio = Audio.objects.get()
            response = json.dumps([{'file_name': audio.file_name,'music_name': audio.name}])
        except:
            response = json.dumps([{'Error': 'no such audio'}])
    return HttpResponse(response,content_type='text/json')
