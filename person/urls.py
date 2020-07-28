from django.urls import path
from person.views import contactView

urlpatterns = [
    path('contacts/', contactView, name='contacts')
]
