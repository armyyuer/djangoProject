# 菜鸟程序员：阿米
from django import template

from common import models
from django.utils.html import format_html
from common.models import Workflow, WorkflowType, WorkflowDef, WorkflowSteps, WorkflowDefSP
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
def splist(value, defid=0):
    qs = WorkflowDefSP.objects.filter(workFlowDefID=defid)
    txt = []
    for m in qs:
        txt.append(m.spName)
    return mark_safe(str(txt))
