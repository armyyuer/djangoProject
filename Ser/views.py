import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
import workflow.views
from Att.views import upload
from common.models import SerOrders, Att, WorkflowSteps, Workflow, WorkflowDef, WorkflowDefSP, UserFlowDef, DDuser, \
    DeptmentUser, \
    UserPosition, SerProject

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

            udcord = UserFlowDef.objects.create(workFlowDefID=d.ID,
                                                status='未执行',
                                                stepsID=0,
                                                deptID=deptID,
                                                deptName=deptName,
                                                spName='',
                                                spID=0)
            UserFlowDefID.append(udcord.ID)
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
                                       userName=checkerName[0:-1],
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
    username = request.session['username']
    print(username)
    steplist = SerOrders.objects.filter(userName__icontains=username).order_by('-orderID')
    # steplist = SerOrders.objects.all().order_by('-orderID')
    print(steplist)
    return render(request, 'ser/myorder.html', {'steplist': steplist})


def myorderinfo(request):
    # working = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    working = range(1, 25)
    print(working, 'working')
    orderID = request.GET.get('orderID')
    Order = SerOrders.objects.get(orderID=orderID)

    deptUser = DeptmentUser.objects.filter(deptID=3)
    print(Order.company)
    try:
        project = SerProject.objects.filter(company=Order.company)
        if project.count() > 0:
            project = SerProject.objects.filter(company=Order.company)
        else:
            project = SerProject.objects.all()
    except SerProject.DoesNotExist:
        project = SerProject.objects.all()
    # print(Order)
    return render(request, 'ser/myorderinfo.html',
                  {'Order': Order, 'project': project, 'deptUser': deptUser, 'working': working})


def myorderinfosave(request):
    now_time = datetime.datetime.now()
    orderID = request.POST.get('orderID')
    lc = request.POST.get('lc')
    if request.POST.get('deptUser'):
        deptUser = request.POST.get('deptUser')
    else:
        deptUser = None
    agree = request.POST.get('agree')
    projectID = request.POST.get('projectID')
    goTime = request.POST.get('goTime')
    workingHours = request.POST.get('workingHours')
    cost = request.POST.get('cost')
    fault = request.POST.get('fault')
    record = request.POST.get('record')
    nextlc = 0
    checkerName = ''
    checkerID = 0
    checkerList = []
    try:
        update = SerOrders.objects.get(orderID=orderID)
    except SerOrders.DoesNotExist:
        print('参数异常！')
    else:
        update = SerOrders.objects.get(orderID=orderID)
        WorkflowStepsID = update.WorkflowStepsID
        ws = WorkflowSteps.objects.get(stepsID=update.WorkflowStepsID)
        print(update.WorkflowStepsID)
        odl = WorkflowDef.objects.filter(workFlowID=ws.workFlowID).order_by('od').last()
        allod = odl.od  # 最后一步
        print(allod, lc, 'yyyyyyyyy')

        if int(lc) == int(allod):  # 如果当前节点是最后一步
            nextlc = -999
            update.lc = nextlc
            update.state = '流程结束'
        else:
            nextlc = int(lc) + 1
            update.lc = nextlc
            print(nextlc, "nextlc")

            checkerName = workflow.views.getspUser(request, ws.workFlowID, lc, nextlc, deptUser, WorkflowStepsID)
            wds = WorkflowDef.objects.get(workFlowID=ws.workFlowID, od=nextlc)
            # update.state = wds.title
            print(checkerName, '下一步审批人!')
            if lc == '1':
                uid = DDuser.objects.get(name=deptUser)
                if agree == '0':
                    nextlc = -1
                    update.lc = nextlc
                    update.state = '不派单'
                    update.agree = agree
                    update.userID = 0
                    update.userName = ''
                    update.seedTime = now_time
                    ws = WorkflowSteps.objects.get(stepsID=WorkflowStepsID)
                    ws.nextID = -1
                    ws.checkerName = ''
                    ws.status = '流程退回'
                    ws.save()
                else:
                    print(lc, "lc == 1")
                    update.repairerID = uid.uid
                    update.repairerName = deptUser  # 维修人员
                    if projectID == 0:
                        update.projectID = 0
                        update.projectName = '无关联项目'
                    else:
                        project = SerProject.objects.get(projectID=projectID)
                        update.projectID = int(projectID)
                        update.projectName = project.projectName
                    update.userID = 0
                    update.userName = checkerName
                    update.seedTime = now_time
                    update.agree = agree
                    update.state = wds.title

            elif lc == '2':
                print(lc, "lc == 2")
                update.goTime = goTime
                update.workingHours = workingHours
                update.cost = cost
                update.endTime = now_time
                update.fault = fault
                update.record = record
                furl = ''
                if request.FILES.get("image"):
                    furl = upload(request.FILES.get("image"), type, request)
                    txt = "上传成功。"
                else:
                    txt = "*清选择要上传的图片!"
                    print(txt)
                update.image = furl
                if int(cost) > 0:
                    update.confirm = 1  # 确认是否维修
                update.userID = 0
                update.userName = checkerName
                update.state = wds.title
            else:
                print(lc, "lc == 其他")

        update.save()

    print(now_time)
    # return render(request, 'ser/myorder.html')
    return HttpResponseRedirect('/ser/myorder/')
