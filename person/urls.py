from django.urls import path
from person.views import index, contactView

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contactView, name='contacts')
]
