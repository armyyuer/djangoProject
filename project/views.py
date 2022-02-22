from django.shortcuts import render
from django.http import HttpResponse

from common import models
from common.models import Project

# Create your views here.

def index_views(request):
    qs = Project.objects.all()
    return render(request, 'project/index.html', {'projectlist': qs})


def projectadd(request):
    return render(request, 'project/add.html')