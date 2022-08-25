from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def type_views(request):
    x = ''
    return render(request, 'workflow/type.html')


def def_views(request):
    x = ''
    return render(request, 'workflow/def.html')


def list(request):
    x = ''
    return render(request, 'workflow/list.html')
