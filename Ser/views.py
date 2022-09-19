import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from common.models import SerOrders, WorkflowSteps, WorkflowDef, WorkflowDefSP, UserFlowDef, DDuser, DeptmentUser, \
    UserPosition

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
    UserFlowDefID = []
    deptName = ''
    deptID = 0
    spName = ''
    spID = 0
    workFlowID = 2
    nextID = 0
    status = ''
    checkerName = ''
    checkerID = 0
    checkerList = []
    odl = WorkflowDef.objects.filter(workFlowID=workFlowID).order_by('od').last()
    allod = odl.od  # 最后一步
    print(allod, 'allod')
    redef = WorkflowDef.objects.filter(workFlowID=workFlowID, od__gt=0).order_by('od')  # >0
    for d in redef:
        # checkerName = d.title
        # checkerID = d.ID
        print(d.title)
        print(d.od)
        print(d.splx)
        print(d.splxName)
        deptID = d.deptid
        deptName = d.deptName
        if d.splx == 2:  # 表单内指定
            print('表单内指定不生成审批人')
        else:  # 指定审批人
            if d.splx == 1:
                spl = WorkflowDefSP.objects.filter(workFlowDefID=d.ID)
                for sp in spl:
                    try:
                        ulist = []
                        udl = UserPosition.objects.filter(positionID=sp.spID, deptID=d.deptid)
                        for ud in udl:
                            ulist.append(ud.userID)
                            print(ulist, 'ulist')
                        try:
                            ul = DDuser.objects.filter(uid__in=ulist)
                            for u in ul:
                                # 生成流程审批人
                                udcord = UserFlowDef.objects.create(workFlowDefID=d.ID,
                                                                    status='未执行',
                                                                    stepsID=0,
                                                                    deptID=deptID,
                                                                    deptName=deptName,
                                                                    spName=u.name,
                                                                    spID=u.uid)
                                UserFlowDefID.append(udcord.ID)

                                # 生成流程审批人
                        except DDuser.DoesNotExist:
                            print('部门' + d.deptName + '无人员信息。')
                    except DeptmentUser.DoesNotExist:
                        print('部门' + d.deptName + '无人员信息。')


                    # print(checkerName[0:-1])
                    # print(checkerID)
            else:
                try:
                    spu = WorkflowDefSP.objects.filter(workFlowDefID=d.ID)
                    for su in spu:
                        # 生成流程审批人
                        udcord = UserFlowDef.objects.create(workFlowDefID=d.ID,
                                                            status='未执行',
                                                            stepsID=0,
                                                            deptID=deptID,
                                                            deptName=deptName,
                                                            spName=su.spName,
                                                            spID=su.spID)
                        UserFlowDefID.append(udcord.ID)
                        # 生成流程审批人
                except WorkflowDefSP.DoesNotExist:
                    response.write("<script>alert('流程配置异常，清联系管理员。');window.location.href='/ser/addflow/';</script>")
                    return response

        if d.od == 1:
            if allod == d.od:  # 如果是最后一步
                status = '流程结束'
                checkerName = ''
                checkerID = 0
                nextID = -999
            else:
                status = d.title
                nextID = d.ID

                if d.splx == 1:
                    spl = WorkflowDefSP.objects.filter(workFlowDefID=d.ID)
                    for sp in spl:
                        try:
                            udlist = []
                            udl = UserPosition.objects.filter(positionID=sp.spID, deptID=d.deptid)
                            for ud in udl:
                                udlist.append(ud.userID)
                                print(udlist, 'udlist')
                            try:
                                ul = DDuser.objects.filter(uid__in=udlist)
                                for u in ul:
                                    checkerName += u.name + ','
                                    checkerList.append(u.uid)
                                    checkerID = checkerList
                                    print(checkerName[0:-1], 'DDuser')
                                    print(checkerID)
                            except DDuser.DoesNotExist:
                                print('部门' + d.deptName + '无人员信息。')
                        except DeptmentUser.DoesNotExist:
                            print('部门' + d.deptName + '无人员信息。')
                        # print(checkerName[0:-1])
                        # print(checkerID)
                else:
                    spl = WorkflowDefSP.objects.filter(workFlowDefID=d.ID)
                    for sp in spl:
                        checkerName += sp.spName + ','
                        checkerList.append(sp.spID)
                        checkerID = checkerList
                        print(checkerName[0:-1])
                        print(checkerID)

    print(UserFlowDefID, 'UserFlowDefID')
    title = company + "提交的售后报修流程。"
    record = WorkflowSteps.objects.create(title=title,
                                          userID=0,
                                          userName=company,
                                          workFlowID=workFlowID,
                                          notes=content,
                                          ip=ip,
                                          itemID=0,
                                          parentID=0,
                                          nextID=nextID,
                                          od=0,
                                          checkerName=checkerName[0:-1],
                                          checkerID=0,
                                          status=status,
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
                                       lc=1,
                                       state=status,
                                       userID=0,
                                       WorkflowStepsID=record.stepsID,
                                       addTime=now_time)
    try:

        for up in UserFlowDefID:
            update = UserFlowDef.objects.get(ID=up)
            update.stepsID = record.stepsID
            update.save()
    except UserFlowDef.DoesNotExist:
        print('异常！')
    print(reOrder.company + "--提交新的报修信息。")
    response.write("<script>alert('报修信息提交成功！');window.location.href='/ser/addflow/';</script>")
    return response


def myorder(request):
    steplist = SerOrders.objects.all()
    return render(request, 'ser/myorder.html', {'steplist': steplist})