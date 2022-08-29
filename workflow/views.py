from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from common.models import WorkflowType


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
    print("修改流程类型：" + str(ID)+"，"+typeName)
    return HttpResponseRedirect('/workflow/type/')


def def_views(request):
    x = ''
    return render(request, 'workflow/def.html')


def wf(request):
    wft = WorkflowType.objects.all()
    return render(request, 'workflow/wf.html', {'typeList': wft})


def wfinfo(request):
    x = ''
    return render(request, 'workflow/wfinfo.html')


def wfdel(request):
    x = ''
    return render(request, 'workflow/wf.html')


def list(request):
    x = ''
    return render(request, 'workflow/list.html')
