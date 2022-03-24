from django.shortcuts import render

# Create your views here.
from common.models import Project


def index_views(request):
    qs = Project.objects.all()
    return render(request, 'orders/index.html', {'projectlist': qs})


def show_views(request):
    pid = request.GET.get("id")
    qs = Project.objects.filter(projectId=pid)
    return render(request, 'orders/show.html', {'Projectdb': qs})
