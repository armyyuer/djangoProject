from django.shortcuts import render


# Create your views here.
from common.models import SerOrders


def index_views(request):
    return render(request, 'ser/index.html')


def addflow(request):
    return render(request, 'ser/addflow.html')


def addflowsave(request):
    company = request.POST.get("company", '')
    address = request.POST.get("address", '')
    contact = request.POST.get("contact", '')
    tel = request.POST.get("tel", '')
    content = request.POST.get("content", '')
    hopeTime = request.POST.get("hopeTime", '')
    remarks = request.POST.get("remarks", '')
    record = SerOrders.objects.create(typeName=typeName)
    print("新增流程类型：" + record.typeName)
    return render(request, 'ser/addflow.html')
