from django.urls import path

from ws.views import workSpaceView

urlpatterns = [
    path('', workSpaceView, name ='workspace')

]
