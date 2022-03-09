from django.shortcuts import render
from django.http import HttpResponse

import common.models
from Att.views import wrdb, upload
from common import models
from common.models import Project, Att, Company, OrderCompany
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# Create your views here.

def index_views(request):
    qs = Project.objects.all().order_by('-projectId')
    return render(request, 'project/index.html', {'projectlist': qs})


def projectadd(request):
    qs = Company.objects.all()
    return render(request, 'project/add.html', {'companylist': qs})


@csrf_exempt
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
    type = request.POST.get("type", '')
    cid = request.POST.getlist("cid", '')
    print("type：" + str(type))
    print("cid：" + str(cid))
    # return HttpResponse(str(cid[0]))

    d1 = timezone.now()
    add_date = d1

    if start_date > end_date:
        return HttpResponse('错误配置！！！开始时间不能大于结束时间 ！！   [ <a href="javascript:history.go(-1)">返回</a> ]')
        # response.write("<script>alert('项目编号已存在！');window.location.href='/project/index/';</script>")
        # return response

    projects = Project.objects.filter(projectNo=projectNo)
    # 如果能找到项目
    if len(projects) > 0:
        return HttpResponse('项目编号已存在！ [ <a href="javascript:history.go(-1)">返回</a> ]')
        # response.write("<script>alert('项目编号已存在！');window.location.href='/project/index/';</script>")
        # return response
    else:
        record = Project.objects.create(projectName=projectName,
                                        projectNo=projectNo,
                                        contacts=contacts,
                                        phone=phone,
                                        type=type,
                                        start_date=start_date,
                                        end_date=end_date,
                                        state=state,
                                        notes=notes,
                                        add_date=add_date)
        # print(request.FILES.get('up_file'))
        furl = upload(request.FILES.get("up_file"))
        print("返回附件路径：" + furl)
        print("项目ID：" + str(record.id))
        # 判断询价类型，如果是邀请报价则添加询价企业
        if type == "0":
            print("询价类型：" + type)
            for name in cid:
                orderCompanyList = []
                print("企业信息循环：" + name)
                companyDB = Company.objects.get(code=name)
                orderCompanyList.append(
                    OrderCompany(companyCode=name, companyName=companyDB.companyName, projectId=record.id, state=0,
                                 up_date=d1)
                )
                print('orderCompanyList数据 ', orderCompanyList)

                try:
                    OrderCompany.objects.bulk_create(orderCompanyList)  # 使用bulk_create批量导入
                    # msg = 'orderCompanyList数据成功'
                except Exception as e:
                    print('orderCompanyList数据异常', e)
                    # msg = 'orderCompanyList数据失败'
        # 判断询价类型，如果是邀请报价则添加询价企业
        wrdb(furl, record.id)  # 附件明细插入数据库
        # print("新增项目：" + record.projectName + ",编号：" + record.projectNo + ",ID：" + str(record.id))
        response.write("<script>alert('项目成功！');window.location.href='/project/index/';</script>")
        return response


def upfile(request):
    return render(request, 'project/upload.html')
