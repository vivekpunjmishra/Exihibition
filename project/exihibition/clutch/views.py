from django.shortcuts import render
from django.http import HttpResponse
from .models import Paintings
# Create your views here.

def home(request):
    paint= Paintings()
    paint.img = 'IMG_6.jpg'
    return render(request,'home.html',{'paint': paint})

def about(request):

    paint = Paintings.objects.all()

    return render(request,'about.html',{'paint': paint})

def store(request):

    paint = Paintings.objects.all()
    return render(request,'store.html',{'paint': paint})

