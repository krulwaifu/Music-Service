import os
import soundfile as sf
import speech_recognition as sr


def handle_uploaded_file(f):
    with open('media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def delete_file(f):
    path = "media/" + f.name
    os.remove(path)


def handle_uploaded_img(f):
    with open('media/images/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def delete_img(f):
    path = "media/images/" + f.name
    os.remove(path)


def convert_file(f):
    data, samplerate = sf.read('media/' + f.name)
    sf.write(os.path.splitext('media/' + f.name)[0] + '.wav', data, samplerate)
    return os.path.splitext('media/' + f.name)[0] + '.wav'
def transcript(f):
    recognizer = sr.Recognizer()
    file = sr.AudioFile('media/' + f.name)
    # file = sr.AudioFile(convert_file(f))
    with file as source:
        audio = recognizer.record(source)
    text = str(recognizer.recognize_google(audio,language="ru-RU"))
    return text

