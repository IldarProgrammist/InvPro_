from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homeapp.urls')),
    path('workspace/', include('ws.urls')),
    path('', include('person.urls')),
    path('product/',include('products.urls')),
    path('', include('ws.urls')),
    path('admin/', admin.site.urls),
]
