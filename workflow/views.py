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
    procedure_choices = [i[1] for i in ulist.choices]
    projects = Deptment.objects.all()

    content = {"username": request.user, "username_data": request.user}
    content['projects'] = projects
    content['procedure_choices'] = procedure_choices
    return render(request, 'workflow/wfinfo.html', content)


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
    return HttpResponseRedirect('/workflow/wfinfo/?ID=' + workFlowID + '')
