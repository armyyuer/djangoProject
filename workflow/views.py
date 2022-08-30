from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from common.models import WorkflowType, Workflow


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


def def_views(request):
    x = ''
    return render(request, 'workflow/def.html')


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
    return render(request, 'workflow/wfinfo.html', {'wfinfo': wf})


def wfinfosave(request):
    x = ''
    return render(request, 'workflow/wfinfo.html')


def wfdel(request):
    ID = request.GET.get("ID", '')
    il = Workflow.objects.get(workflowID=ID).delete()
    return HttpResponseRedirect('/workflow/wf/')


def list(request):
    x = ''
    return render(request, 'workflow/list.html')
