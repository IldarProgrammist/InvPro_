from django.shortcuts import render


def workSpaceView(request):

    return render(request, 'ws/WorkSpace.html')