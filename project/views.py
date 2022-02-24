from django.shortcuts import render
from django.http import HttpResponse

from common import models
from common.models import Project
from django.utils import timezone


# Create your views here.

def index_views(request):
    qs = Project.objects.all()
    return render(request, 'project/index.html', {'projectlist': qs})


def projectadd(request):
    return render(request, 'project/add.html')


def projectaddsave(request):
    response = HttpResponse()
    projectName = request.POST.get("projectName", '')
    projectNo = request.POST.get("projectNo", '')
    contacts = request.POST.get("contacts", '')
    phone = request.POST.get("phone", '')
    start_date = request.POST.get("start_date", '')
    end_date = request.POST.get("end_date", '')
    state = request.POST.get("state", '')
    notes = request.POST.get("notes", '')
    d1 = timezone.now()
    add_date = d1

    if start_date > end_date:
        return HttpResponse('错误配置！！！开始时间不能大于结束时间 ！！   [ <a href="javascript:history.go(-1)">返回</a> ]')
        # response.write("<script>alert('项目编号已存在！');window.location.href='/project/index/';</script>")
        return response

    projects = Project.objects.filter(projectNo=projectNo)
    # 如果能找到项目
    if len(projects) > 0:
        return HttpResponse('项目编号已存在！ [ <a href="javascript:history.go(-1)">返回</a> ]')
        # response.write("<script>alert('项目编号已存在！');window.location.href='/project/index/';</script>")
        return response
    else:
        record = Project.objects.create(projectName=projectName,
                                        projectNo=projectNo,
                                        contacts=contacts,
                                        phone=phone,
                                        start_date=start_date,
                                        end_date=end_date,
                                        state=state,
                                        notes=notes,
                                        add_date=add_date)

        print("新增项目：" + record.projectName + ",编号：" + record.projectNo + ",ID：" + str(record.id))
        response.write("<script>alert('项目成功！');window.location.href='/project/index/';</script>")
        return response
