from django.urls import path

from products.views import workSpaceWiew

urlpatterns = [
    path('workspace/', workSpaceWiew, name ='workspace')

]
