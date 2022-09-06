# 菜鸟程序员：阿米
from django import template

from common import models
from django.utils.html import format_html
from common.models import Workflow, WorkflowType, WorkflowDef, WorkflowSteps, WorkflowDefSP, DeptmentUser
from django.utils.safestring import mark_safe

# 下面代码会直接使用register
register = template.Library()


@register.filter
def wflist(value, pid=0):
    qs = Workflow.objects.filter(typeID=pid)
    txt = ""
    for m in qs:
        txt += "<tr>"
        txt += "<td>" + str(m.workflowID) + "</td>"
        txt += "<td>" + str(m.name) + "</td>"
        txt += "<td class=\"text-navy\">"
        txt += "<a href=\"/workflow/wfinfo/?ID=" + str(m.workflowID) + "\" ><i class=\"fa fa-pencil\"></i>编辑</a> |"
        txt += "<a href=\"javascript:deleteRecord(" + str(m.workflowID) + ")\" ><i class=\"fa fa-trash-o\"></i>删除</a>"
        txt += "</td>"
        txt += "</tr>"
    return mark_safe(txt)


@register.filter
def splist(value=0, defid=0):
    if value == 2:
        txt = '表单内指定'
    else:
        qs = WorkflowDefSP.objects.filter(workFlowDefID=defid)
        txt = []
        for m in qs:
            txt.append(m.spName)
    return mark_safe(str(txt))


@register.filter
def ulist_e(deptID=0, defid=0):
    print(str(defid),'defid')
    qs = DeptmentUser.objects.filter(deptID=deptID)
    html = ''
    for m in qs:
        html += "<option value="+str(m.userID)
        defs = WorkflowDefSP.objects.filter(workFlowDefID=defid)
        for d in defs:
            if d.spID == m.userID:
                html += " selected"
        html += ">"+m.userName+"</option>"
    return mark_safe(str(html))


@register.filter
def plist_e(defID=0, positionID=0):
    html = ''
    defs = WorkflowDefSP.objects.filter(workFlowDefID=defID)
    for d in defs:
        if d.spID == positionID:
            html += " selected"
    return mark_safe(str(html))
