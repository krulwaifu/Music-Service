from django.http import HttpResponse
import json

from django.shortcuts import render
from django.template import RequestContext

from audio.forms import AudioForm
from audio.functions import handle_uploaded_file, delete_file
from audio.models import Audio

def get_audio(request,name):
    global response
    if request.method == "GET":
        context = {'audios': Audio.objects.filter(name = name),
                   'title': 'audios'}
        return render(request, 'showAudio.html', context)

def get_all_audio(request):
    global response
    if request.method == "GET":
        context = {'audios': Audio.objects.all(),
                   'title': 'audios'}
    return render(request,'showAudio.html', context)

def upload(request):
    if request.method == 'POST':
        audio = AudioForm(request.POST,request.FILES)
        if audio.is_valid():
            handle_uploaded_file(request.FILES['file'])
            model_instance = audio.save(commit=False)
            model_instance.save()
            return HttpResponse("file uploaded successfully")
    else:
        audio = AudioForm()
        return render(request, 'upload.html', {'form':audio})
def edit_name(request,name,new_name):
    if request.method == "GET":
        audio = Audio.objects.get(name = name)
        audio.name = new_name
        audio.save(update_fields=["name"])
    return HttpResponse("file edited successfully")

def delete(request,name):
    if request.method == "GET":
        audio = Audio.objects.get(name = name)
        delete_file(audio.file)
        audio.delete()
    return HttpResponse("file deleted successfully")