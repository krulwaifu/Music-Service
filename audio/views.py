from django.contrib.auth import get_user_model
from django.http import HttpResponse
import json

from django.shortcuts import render
from django.template import RequestContext

from audio.forms import AudioForm
from audio.functions import handle_uploaded_file, delete_file, handle_uploaded_img, delete_img
from audio.models import Audio

def get_audio(request,name):
    global response
    if request.method == "GET":
        context = {'audios': Audio.objects.filter(name = name),
                   'title': 'audios'}
        return render(request, 'audioPage.html', context)
def get_audio_byUserId(request,id):
    global response
    if request.method == "GET":
        User = get_user_model()
        users = User.objects.get(id=int(id))
        list = [users]
        context1 = {'audios': Audio.objects.filter(user_id = id),
                   'title': 'audizos'}
        context = {'users': list,
                   'title': 'users'}
        return render(request, 'userPage.html', {'audios': Audio.objects.filter(user_id = id), 'users': list})

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
            handle_uploaded_img(request.FILES['image'])
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
        delete_img(audio.image)
        audio.delete()
    context = {'message': "Audio deleted successfully",
               'title': 'message'}
    return render(request, 'showAudio.html', context)

def musicpage(request):
    return render(request,'music_player.html')