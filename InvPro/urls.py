from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homeapp.urls')),
    path('person/', include('person.urls')),
    path('admin/', admin.site.urls),
    path('act/', include('act.urls')),
]
