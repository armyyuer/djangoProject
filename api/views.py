from django.shortcuts import render
# from api.ccgp import seedtxt


# Create your views here.

def userinfo(request):
    return render(request, 'api/ccgp.html')


def ccgpseed(request):
    return render(request, 'api/ccgp.html')
