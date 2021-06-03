from django.contrib.auth import get_user_model
from django.http import HttpResponse
import json
import speech_recognition as sr

from django.shortcuts import render
from django.template import RequestContext

from audio.forms import AudioForm, TranscriptionFormC, TranscriptionFormS
from audio.functions import handle_uploaded_file, delete_file, handle_uploaded_img, delete_img, convert_file, transcript
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

def speech_to_text(request):
    if request.method == 'POST':
        audio_id = int(request.POST.__getitem__('audio'))
        audio = Audio.objects.get(id = audio_id)
        text = transcript(audio.file)
        transcription = TranscriptionFormS(request.POST, text)
        if transcription.is_valid():
            model_instance = transcription.save(commit=False)
            model_instance.save()
        return render(request,'textSpeech.html',{'text': "Google Speech Recognition thinks the text is: " + text})
    else:
        transcription = TranscriptionFormC()
        return render(request,'textSpeech.html',{'form':transcription})
def speech_to_text_save(request):
    if request.method == 'POST':
        transcription = TranscriptionFormS(request.POST)
        if transcription.is_valid():
            model_instance = transcription.save(commit=False)
            model_instance.save()
        return render(request,'textSpeechSave.html',{'text': "text was saved"})
    else:
        transcription = TranscriptionFormS()
        return render(request,'textSpeechSave.html',{'form':transcription})

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