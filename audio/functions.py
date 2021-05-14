import os


def handle_uploaded_file(f):
    with open('audio/uploads/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def delete_file(f):
    path = "audio/uploads/"+f.name
    os.remove(path)