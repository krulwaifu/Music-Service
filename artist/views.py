from django.shortcuts import render

# Create your views here.
def art(request):
    return render(request,'artist.html')