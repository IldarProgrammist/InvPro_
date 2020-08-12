from django.urls import path
from person.views import contactView

urlpatterns = [
    path('person/', contactView, name ='person')
   # path('persons/',contactView, name = 'person')

]
