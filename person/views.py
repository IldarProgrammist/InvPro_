from django.shortcuts import render
from .models import *
from django.db.models import Q


def index(request):
   return render(request, 'index.html')


def contactView(request):
   searchQwery = request.GET.get('search','')

   if searchQwery:
      persons = Person.objects.filter(Q(firstName__icontains=searchQwery)|Q(lastName__icontains=searchQwery))
   else:
      persons = Person.objects.all().order_by('firstName')

   return render(request, 'person/contct.html', {'persons': persons})


