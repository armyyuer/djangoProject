from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_views(request):
    return render(request, 'project/index.html')
