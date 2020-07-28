from django.shortcuts import render

from eq.models import ModelsE


def eqListView(request):

    eq = ModelsE.objects.all()

    context ={
        'eq' : eq
    }
    return render(request, 'eq/eq.html', context)