from django.shortcuts import render
from .models import *


def index(request):
   return render(request, 'index.html')


def contactView(request):
   persons = Person.objects.all()
   return render(request, 'person/contct.html', {'persons': persons})


