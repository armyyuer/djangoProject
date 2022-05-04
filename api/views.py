from django.shortcuts import render


# Create your views here.

def userinfo(request):
    return render(request, 'userinfo.html')
