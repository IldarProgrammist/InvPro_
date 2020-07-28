from django.urls import path

from homeapp.views import index

urlpatterns = [
    path('', index, name='home'),
]
