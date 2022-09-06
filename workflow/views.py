from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from common.models import WorkflowType, Workflow, Deptment, DeptmentUser, Position, WorkflowDef, WorkflowDefSP, DDuser


def type_views(request):
    qs = WorkflowType.objects.all().order_by("ID")
    return render(request, 'workflow/type.html', {'TypeList': qs})


def typeadd(request):
    typeName = request.POST.get("typeName", '')
    record = WorkflowType.objects.create(typeName=typeName)
    print("新增流程类型：" + record.typeName)
    return HttpResponseRedirect('/workflow/type/')


def typedel(request):
    ID = request.GET.get('ID')
    il = WorkflowType.objects.get(ID=ID).delete()
    return HttpResponseRedirect('/workflow/type/')


def typeedit(request):
    ID = request.GET.get('ID')
    il = WorkflowType.objects.get(ID=ID)
    return render(request, 'workflow/typeedit.html', {'typeinfo': il})


def typeeditsave(request):
    typeName = request.POST.get("typeName", '')
    ID = request.POST.get("ID", '')
    try:
        # 根据 id 从数据库中找到相应的户记录
        update = WorkflowType.objects.get(ID=ID)
        update.typeName = typeName
        update.save()
    except WorkflowType.DoesNotExist:
        print("不存在" + str(ID))
    print("修改流程类型：" + str(ID) + "，" + typeName)
    return HttpResponseRedirect('/workflow/type/')


def wf(request):
    wft = WorkflowType.objects.all()
    return render(request, 'workflow/wf.html', {'typeList': wft})


def wfadd(request):
    wft = WorkflowType.objects.all()
    return render(request, 'workflow/wfadd.html', {'typeList': wft})


def wfaddsave(request):
    typeID = request.POST.get("typeID", '')
    type = WorkflowType.objects.get(ID=typeID)
    typeName = type.typeName
    name = request.POST.get("name", '')
    record = Workflow.objects.create(typeID=typeID,
                                     typeName=typeName,
                                     name=name)
    print("新增流程配置：" + record.name)
    return HttpResponseRedirect('/workflow/wf/')


def wfinfo(request):
    ID = request.GET.get("ID", '')
    wf = Workflow.objects.get(workflowID=ID)
    depList = Deptment.objects.all()
    positionList = Position.objects.all()
    defList = ''
    try:
        defList = WorkflowDef.objects.order_by('od').filter(workFlowID=ID)
        print(defList)
    except WorkflowDef.DoesNotExist:
        defList = None
        print(defList)
    return render(request, 'workflow/wfinfo.html',
                  {'wfinfo': wf, 'depList': depList, 'positionList': positionList, 'defList': defList})


def ulist(request):
    deptID = request.GET.get('deptID')
    if deptID:
        users = DeptmentUser.objects.filter(deptID=deptID)
        print(users, 'users')
        result = serialize("json", users)
        print(result, 'result')
        return HttpResponse(result)
    # procedure_choices = [i[1] for i in ulist.choices]
    # projects = Deptment.objects.all()
    #
    # content = {"username": request.user, "username_data": request.user}
    # content['projects'] = projects
    # content['procedure_choices'] = procedure_choices
    # return render(request, 'workflow/wfinfo.html', content)


def wfinfosave(request):
    workFlowID = request.POST.get("workFlowID", '')
    title = request.POST.get("title", '')
    od = request.POST.get("od", '')
    splx = request.POST.get("splx", '')
    deptID = request.POST.get("deptID", '')
    empower_user = request.POST.getlist("empower_user", '')
    return HttpResponseRedirect('/workflow/wfinfo/?ID=1')


def wfdel(request):
    ID = request.GET.get("ID", '')
    il = Workflow.objects.get(workflowID=ID).delete()
    return HttpResponseRedirect('/workflow/wf/')


def list(request):
    x = ''
    return render(request, 'workflow/list.html')


def def_views(request):
    x = ''
    return render(request, 'workflow/def.html')


def defaddsave(request):
    workFlowID = request.POST.get("workFlowID", '')
    title = request.POST.get("title", '')
    od = request.POST.get("od", '')
    splx = request.POST.get("splx", '')
    deptID = "0"
    empower_user = '0'
    positionID = '0'
    splxName = '指定审批人'
    if splx == "0":
        deptID = request.POST.get("deptID", '')
        dep = Deptment.objects.get(deptID=deptID)
        empower_user = request.POST.getlist("empower_user", '')
        us = DDuser.objects.filter(uid__in=empower_user)
        print(empower_user, 'empower_user')
        print(workFlowID, 'workFlowID')
        print(dep.deptName, 'deptName')
        # print(us, 'us')
        splxName = '指定审批人'
        record = WorkflowDef.objects.create(workFlowID=workFlowID,
                                            title=title,
                                            od=od,
                                            splx=splx,
                                            splxName=splxName,
                                            deptid=deptID,
                                            deptName=dep.deptName)
        print("新增流程指定人审批节点：" + od + "---" + record.title)

        for u in us:
            resp = WorkflowDefSP.objects.create(workFlowDefID=record.ID,
                                                spName=u.name,
                                                spID=u.uid)
            print("新增节点指定审批人：" + resp.spName)
    elif splx == "1":
        splxName = '指定部门职务'
        deptID = request.POST.get("deptID_", '')
        dep = Deptment.objects.get(deptID=deptID)
        positionID = request.POST.getlist("positionID", '')
        us = Position.objects.filter(positionID__in=positionID)
        print(positionID, 'positionID')
        record = WorkflowDef.objects.create(workFlowID=workFlowID,
                                            title=title,
                                            od=od,
                                            splx=splx,
                                            splxName=splxName,
                                            deptid=deptID,
                                            deptName=dep.deptName)
        print("新增流程职务审批节点：" + od + "---" + record.title)

        for u in us:
            resp = WorkflowDefSP.objects.create(workFlowDefID=record.ID,
                                                spName=u.positionName,
                                                spID=u.positionID)
            print("新增节点指定审批职务：" + resp.spName)
    else:
        splxName = '表单内指定'
        deptID = 0
        positionID = 0
        record = WorkflowDef.objects.create(workFlowID=workFlowID,
                                            title=title,
                                            od=od,
                                            splx=splx,
                                            splxName=splxName,
                                            deptid=deptID)
        print("新增流程表单内指定审批节点：" + od + "---" + record.title)
    return HttpResponseRedirect('/workflow/wfinfo/?ID=' + workFlowID + '')


def defeditsave(request):
    ID_e = request.POST.get("ID_e", '')
    workFlowID_e = request.POST.get("workFlowID_e", '')
    title_e = request.POST.get("title_e", '')
    od_e = request.POST.get("od_e", '')
    splx_e = request.POST.get("splx_e", '')
    deptID_e = "0"
    empower_user_e = '0'
    positionID_e = '0'
    splxName_e = '指定审批人'
    if splx_e == "0":
        deptID_e = request.POST.get("deptID_e", '')
        dep = Deptment.objects.get(deptID=deptID_e)
        empower_user_e = request.POST.getlist("empower_user_e", '')
        us = DDuser.objects.filter(uid__in=empower_user_e)
        print(empower_user_e, 'empower_user_e')
        print(workFlowID_e, 'workFlowID_e')
        print(dep.deptName, 'deptName_e')
        # print(us, 'us')
        splxName_e = '指定审批人'

        try:
            # 根据 id 从数据库中找到相应的户记录
            update = WorkflowDef.objects.get(ID=ID_e)
            update.workFlowID = workFlowID_e
            update.title = title_e
            update.od = od_e
            update.splx = splx_e
            update.splxName = splxName_e
            update.deptid = deptID_e
            update.deptName = dep.deptName
            update.save()
        except WorkflowType.DoesNotExist:
            print("不存在" + str(ID_e))
        print("修改流程指定人审批节点：" + od_e + "---" + title_e)

        try:
            il = WorkflowDefSP.objects.filter(workFlowDefID=ID_e).delete()
        except WorkflowDefSP.DoesNotExist:
            print("不存在" + str(ID_e))
        for u in us:
            resp = WorkflowDefSP.objects.create(workFlowDefID=ID_e,
                                                spName=u.name,
                                                spID=u.uid)
            print("修改节点指定审批人：" + resp.spName)
    elif splx_e == "1":
        splxName_e = '指定部门职务'
        deptID_e = request.POST.get("deptID_e_", '')
        dep = Deptment.objects.get(deptID=deptID_e)
        positionID_e = request.POST.getlist("positionID_e", '')
        us = Position.objects.filter(positionID__in=positionID_e)
        print(positionID_e, 'positionID_e')
        try:
            # 根据 id 从数据库中找到相应的户记录
            update = WorkflowDef.objects.get(ID=ID_e)
            update.workFlowID = workFlowID_e
            update.title = title_e
            update.od = od_e
            update.splx = splx_e
            update.splxName = splxName_e
            update.deptid = deptID_e
            update.deptName = dep.deptName
            update.save()
        except WorkflowType.DoesNotExist:
            print("不存在" + str(ID_e))
        print("修改流程指定人审批节点：" + od_e + "---" + title_e)

        try:
            il = WorkflowDefSP.objects.filter(workFlowDefID=ID_e).delete()
        except WorkflowDefSP.DoesNotExist:
            print("不存在" + str(ID_e))

        for u in us:
            resp = WorkflowDefSP.objects.create(workFlowDefID=ID_e,
                                                spName=u.positionName,
                                                spID=u.positionID)
            print("修改节点指定审批职务：" + resp.spName)
    else:
        splxName_e = '表单内指定'
        deptID_e = 0
        positionID_e = 0
        try:
            # 根据 id 从数据库中找到相应的户记录
            update = WorkflowDef.objects.get(ID=ID_e)
            update.workFlowID = workFlowID_e
            update.title = title_e
            update.od = od_e
            update.splx = splx_e
            update.splxName = splxName_e
            update.deptid = deptID_e
            update.save()
        except WorkflowType.DoesNotExist:
            print("不存在" + str(ID_e))
        print("修改流程指定人审批节点：" + od_e + "---" + title_e)

        try:
            il = WorkflowDefSP.objects.filter(workFlowDefID=ID_e).delete()
        except WorkflowDefSP.DoesNotExist:
            print("不存在" + str(ID_e))

    return HttpResponseRedirect('/workflow/wfinfo/?ID=' + workFlowID_e + '')


def defdel(request):
    ID = request.GET.get("ID", '')
    il = WorkflowDef.objects.get(ID=ID)
    workFlowID = il.workFlowID
    il.delete()
    return HttpResponseRedirect('/workflow/wfinfo/?id=' + workFlowID)
