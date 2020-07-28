from django.urls import path
from eq.views import eqListView


urlpatterns = [
    path('eq/', eqListView, name='eq')
]
