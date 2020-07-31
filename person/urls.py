from django.urls import path
from person.views import contactView

urlpatterns = [
    path('', contactView, name='contacts')
]
