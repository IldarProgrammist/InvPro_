from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homeapp.urls')),
    path('', include('person.urls')),
    path('', include('eq.urls')),
    path('admin/', admin.site.urls),
]
