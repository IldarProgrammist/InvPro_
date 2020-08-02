from django.urls import path
# from person.views import contactView
from person.views import personList

urlpatterns = [
    path('person/', personList.as_view(), name ='person')
   # path('persons/',contactView, name = 'person')

]
