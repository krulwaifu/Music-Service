import os


def handle_uploaded_file(f):
    with open('media/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def delete_file(f):
    path = "media/"+f.name
    os.remove(path)

def handle_uploaded_img(f):
    with open('media/images/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def delete_img(f):
    path = "media/images/"+f.name
    os.remove(path)