from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def desktop_views(request):
    return render(request, 'main/desktop.html')
