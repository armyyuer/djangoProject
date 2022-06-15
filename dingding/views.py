from django.shortcuts import render


# Create your views here.

def dingding_index(request):
    return render(request, 'dingding/index.html')
