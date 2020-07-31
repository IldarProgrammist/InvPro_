from django.urls import path

from act.views import ListActView
from homeapp.views import index

urlpatterns = [
    path('', ListActView, name='act'),
]
