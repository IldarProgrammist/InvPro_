from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django.db.models import Q



"""Простой поиск по фамилии и имени"""
def contactView(request):

   searchQwery = request.GET.get('search','')
   if searchQwery:
      persons = Person.objects.filter(Q(firstName__icontains=searchQwery)|Q(lastName__icontains=searchQwery))
   else:
      persons = Person.objects.all().order_by('firstName')

   page_number = request.GET.get('page',1)
   paginator = Paginator(persons,4)
   page = paginator.get_page(page_number)

   is_paginated = page.has_other_pages()

   if page.has_previous():
      prev_url = '?page{}'.format(page.previous_page_number())
   else: prev_url = ''

   if page.has_next():
      next_url = '?page{}'.format(page.next_page_number())
   else:
      next_url = ''



   context = {
      'persons' : page,
      'is_paginated':is_paginated,
      'next_url' :next_url,
      'prev_url': prev_url
      }




   return render(request, 'person/person.html', context =context)





# class personList(ListView):
#    model = Person
#    context_object_name = 'persons'
#    paginate_by = 4
#    template_name ='person/person.html'
#    queryset = Person.objects.order_by('firstName')












