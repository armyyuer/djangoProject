import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from common.models import SerOrders, WorkflowSteps, WorkflowDef

response = HttpResponse()


def index_views(request):
    return render(request, 'ser/index.html')


def addflow(request):
    return render(request, 'ser/addflow.html')


def addflowsave(request):
    ip = request.META['REMOTE_ADDR']
    now_time = datetime.datetime.now()
    company = request.POST.get("company", '')
    address = request.POST.get("address", '')
    contact = request.POST.get("contact", '')
    tel = request.POST.get("tel", '')
    content = request.POST.get("content", '')
    hopeTime = request.POST.get("hopeTime", '')
    remarks = request.POST.get("remarks", '')
    workFlowID = 2
    checkerName = ''
    checkerID=0
    redef = WorkflowDef.objects.filter(workFlowID=workFlowID, od=1).order_by('od')  # >0
    for d in redef:
        checkerName = d.title
        checkerID = d.ID
        print(d.title)
    title = company + "提交的售后报修流程。"
    record = WorkflowSteps.objects.create(title=title,
                                          userID=0,
                                          userName=company,
                                          workFlowID=workFlowID,
                                          notes=content,
                                          ip=ip,
                                          itemID=0,
                                          parentID=0,
                                          nextID=0,
                                          od=0,
                                          checkerName=checkerName,
                                          checkerID=checkerID,
                                          status=checkerName,
                                          typeID=2,
                                          addTime=now_time)
    reOrder = SerOrders.objects.create(company=company,
                                       address=address,
                                       contact=contact,
                                       tel=tel,
                                       content=content,
                                       hopeTime=hopeTime,
                                       remarks=remarks,
                                       projectID=0,
                                       repairerID=0,
                                       workingHours=0,
                                       cost=0,
                                       lc=0,
                                       state=checkerName,
                                       userID=0,
                                       WorkflowStepsID=record.stepsID,
                                       addTime=now_time)
    print(reOrder.company + "--提交新的报修信息。")
    response.write("<script>alert('报修信息提交成功！');window.location.href='/ser/addflow/';</script>")
    return response
