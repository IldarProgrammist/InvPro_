from django.urls import path
from act.views import ListActView, aplictionsListView


urlpatterns = [
    path('', ListActView, name='act'),
    path('app/', aplictionsListView, name='app')
]
