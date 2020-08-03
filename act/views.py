from django.shortcuts import render

from act.models import Act, Application, Extradition


def ListActView(request):

   extradition =Extradition.objects.all()

   return render(request, 'act/listAct.html', {'extradition':extradition})



def aplictionsListView(request):
   ap = Application.objects.all()
   return  render(request, 'act/aplications.html',{'app':ap})