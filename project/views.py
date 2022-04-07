from django.shortcuts import render
from django.http import HttpResponse

import common.models
from Att.views import wrdb, upload
from common import models
from common.models import Project, Att, Company, OrderCompany, ProjectItem, Unit
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
        print("项目ID：" + str(record.projectId))
        # 判断询价类型，如果是邀请报价则添加询价企业
        if type == "0":
            print("询价类型：" + type)
            for name in cid:
                orderCompanyList = []
                print("企业信息循环：" + name)
                companyDB = Company.objects.get(code=name)
                orderCompanyList.append(
                    OrderCompany(companyCode=name, companyName=companyDB.companyName, projectId=record.projectId,
                                 state=0,
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
        wrdb(furl, record.projectId)  # 附件明细插入数据库
        # print("新增项目：" + record.projectName + ",编号：" + record.projectNo + ",ID：" + str(record.id))
        response.write("<script>alert('项目添加成功成功！');window.location.href='/project/index/';</script>")
        return response


def upfile(request):
    return render(request, 'project/upload.html')


def projectItemadd(request):
    response = HttpResponse()
    furl = upload(request.FILES.get("up_file"))
    pid = request.POST.get("pid")
    if furl:
        print("返回附件路径：" + furl)
        wrdb(furl, pid)  # 附件明细插入数据库
        response.write("<script>alert('明细表导入成功！');window.location.href='/project/edit/?id=" + str(pid) + "';</script>")
    else:
        response.write(
            "<script>alert('请选择需要导入的明细表！');window.location.href='/project/edit/?id=" + str(pid) + "';</script>")

    return response


def delete(request):
    pid = request.GET.get('id')
    us = Project.objects.get(projectId=pid)
    us.delete()
    du = ProjectItem.objects.filter(projectId=pid)
    du.delete()

    return render(request, 'project/index.html', {'projectid': pid})


def edit_views(request):
    pid = request.GET.get('id')
    qs = Company.objects.all()
    dw = Unit.objects.all()
    oc = OrderCompany.objects.filter(projectId=pid)
    pdb = Project.objects.filter(projectId=pid)
    pidb = ProjectItem.objects.filter(projectId=pid)
    return render(request, 'project/edit.html',
                  {'companylist': qs, 'OClist': oc, 'Projectdb': pdb, 'Itemdb': pidb, 'pid': pid, 'unitList': dw})


def editsave(request):
    global update
    response = HttpResponse()
    projectId = request.POST.get("projectId")
    projectName = request.POST.get("projectName")
    projectNo = request.POST.get("projectNo")
    contacts = request.POST.get("contacts")
    phone = request.POST.get("phone")
    start_date = request.POST.get("start_date")
    end_date = request.POST.get("end_date")
    state = request.POST.get("state")
    notes = request.POST.get("notes")
    p_type = request.POST.get("type")
    cid = request.POST.getlist("cid")
    print("type：" + str(p_type))
    print("cid：" + str(cid))
    print("notes：" + str(notes))
    # return HttpResponse(str(cid[0]))

    d1 = timezone.now()
    up_date = d1
    # updb = {"projectName": projectName, "projectNo": projectNo, "contacts": contacts, "phone": phone, "p_type": p_type,
    #         "start_date": start_date, "end_date": end_date, "state": state, "notes": notes, "up_date": up_date}
    #
    #
    # print(str(updb))
    # print(str(updb['projectName']))
    if start_date > end_date:
        return HttpResponse('错误配置！！！开始时间不能大于结束时间 ！！   [ <a href="javascript:history.go(-1)">返回</a> ]')
    try:
        # 根据 id 从数据库中找到相应的户记录
        update = Project.objects.get(projectId=projectId)
    except Project.DoesNotExist:
        print("Project不存在" + str(type))
    # update.projectName = updb["projectName"]
    # update.projectNo = updb["projectNo"]
    # update.contacts = updb["contacts"]
    # update.phone = updb["phone"]
    # update.type = updb["p_type"]
    # update.start_date = updb["start_date"]
    # update.end_date = updb["end_date"]
    # update.state = updb["state"]
    # update.notes = updb["notes"]
    # update.up_date = updb["up_date"]
    update.projectName = projectName
    update.projectNo = projectNo
    update.contacts = contacts
    update.phone = phone
    update.type = p_type
    update.start_date = start_date
    update.end_date = end_date
    update.state = state
    update.notes = notes
    update.up_date = up_date
    update.save()

    print("项目ID：" + str(projectId))
    # 判断询价类型，如果是邀请报价则添加询价企业
    if type == "0":
        print("询价类型：" + p_type)

        companyDB = OrderCompany.objects.filter(projectId=projectId)
        if companyDB:
            OrderCompany.objects.get(projectId=projectId).delete()

        for name in cid:
            orderCompanyList = []
            print("企业信息循环：" + name)
            companyDB = Company.objects.get(code=name)
            orderCompanyList.append(
                OrderCompany(companyCode=name, companyName=companyDB.companyName, projectId=projectId,
                             state=0,
                             up_date=d1)
            )
            print('orderCompanyList数据 ', orderCompanyList)

            try:
                OrderCompany.objects.bulk_create(orderCompanyList)  # 使用bulk_create批量导入
                # msg = 'orderCompanyList数据成功'
            except Exception as e:
                print('orderCompanyList数据异常', e)
                # msg = 'orderCompanyList数据失败'
    response.write("<script>alert('提交成功！');window.location.href='/project/index/';</script>")
    return response


def edititemsave(request):
    global update
    response = HttpResponse()
    projectId = request.POST.get("projectId")
    itemID = request.POST.get("itemID")
    itemName = request.POST.get("itemName")
    Specs = request.POST.get("Specs")
    Brand = request.POST.get("Brand")
    Unit = request.POST.get("Unit")
    Count = request.POST.get("Count")
    d1 = timezone.now()
    up_date = d1
    try:
        # 根据 id 从数据库中找到相应的户记录
        update = ProjectItem.objects.get(itemID=itemID)
    except Project.DoesNotExist:
        print("ProjectItem不存在" + str(itemName))
    update.itemName = itemName
    update.Specs = Specs
    update.Brand = Brand
    update.Unit = Unit
    update.Count = Count
    update.up_date = up_date
    update.save()
    response.write("<script>alert('修改成功！');window.location.href='/project/edit/?id=" + projectId + "';</script>")
    return response


def additemsave(request):
    global updat
    response = HttpResponse()
    projectId = request.POST.get("projectId")
    itemName = request.POST.get("itemName")
    Count = request.POST.get("Count")
    Unit = request.POST.get("Unit")
    Specs = request.POST.get("Specs")
    Brand = request.POST.get("Brand")
    d1 = timezone.now()
    up_date = d1

    record = ProjectItem.objects.create(projectId=projectId,
                                        itemName=itemName,
                                        Count=Count,
                                        Unit=Unit,
                                        Specs=Specs,
                                        Brand=Brand,
                                        up_date=up_date,
                                        add_date=up_date)

    response.write("<script>alert('新增成功！ID："+str(record.itemID)+"。');window.location.href='/project/edit/?id="
                   + projectId + "';</script>")
    return response


def deleteitem(request):
    response = HttpResponse()
    id = request.GET.get('id')
    us = ProjectItem.objects.get(itemID=id)
    pid = us.projectId
    du = ProjectItem.objects.get(itemID=id)
    du.delete()

    response.write("<script>alert('删除成功！');window.location.href='/project/edit/?id=" + str(pid) + "';</script>")
    return response
