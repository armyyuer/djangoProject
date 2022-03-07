import os

import uuid
import xlrd
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
# from pip._internal.resolution.resolvelib.resolver import Result

from Att import models
from common.models import Project, Att, ProjectItem

# Create your views here.
from djangoProject import settings
from django.utils import timezone
from openpyxl import load_workbook


# def __init__(self, itemName):
#     self.ItemName = itemName
#
# def learn(self):
#     print('%s is learning' % self.itemName

# @csrf_exempt
def up_file_excel(file):
    # 根name取 file 的值
    # logger.log().info('uplaod:%s' % file)
    # 创建upload文件夹
    furl = ""
    if not os.path.exists(settings.UPLOAD_ROOT):
        os.makedirs(settings.UPLOAD_ROOT)
    try:
        if file is None:
            return HttpResponse('请选择要上传的文件')
        # 循环二进制写入
        furl = settings.UPLOAD_ROOT + "/" + file.name
        print(furl)
        with open(settings.UPLOAD_ROOT + "/" + file.name, 'wb') as f:
            for i in file.readlines():
                f.write(i)
    except Exception as e:
        return HttpResponse(e)

    # return HttpResponse('上传成功')
    return furl


# 将excel数据写入mysql
# @staticmethod  #静态方法
# @classmethod#类方法
def wrdb(file, projectId):
    d1 = timezone.now()
    # print(myform)
    print("file:" + file)

    # 删除projectId明细
    # df = Att.objects.get(projectId=projectId)
    # df.delete()
    # 打开上传 excel 表格
    # readboot = xlrd.open_workbook(settings.UPLOAD_ROOT + file)
    # sheet = readboot.sheet_by_index(0)
    # # 获取excel的行和列
    # nrows = sheet.nrows
    # ncols = sheet.ncols
    # print(ncols, nrows)
    # for i in range(1, nrows):
    #     row = sheet.row_values(i)
    #     itemName = row[1]
    #     Specs = row[2]
    #     Brand = row[3]
    #     Unit = row[4]
    #     Count = row[5]
    #     Tax = 0
    #     add_date = d1
    #     up_date = d1
    #
    #     record = ProjectItem.objects.create(projectId=projectId,
    #                                         itemName=itemName,
    #                                         Specs=Specs,
    #                                         Brand=Brand,
    #                                         Unit=Unit,
    #                                         Count=Count,
    #                                         Tax=Tax,
    #                                         add_date=add_date,
    #                                         up_date=up_date)
    #     print("插入明细:" + itemName + ",ID：" + record.itemID)

    wb = load_workbook(filename=settings.UPLOAD_ROOT + file)  # 打开文件,默认可读写，若有需要可以指定write_only和read_only为True
    ws = wb.active  # 拿到默认的sheet工作表
    max_row = ws.max_row  # 拿到总行数
    max_column = ws.max_column  # 拿到总列数
    print("sheet:" + str(max_row))
    print("sheetvalue:" + str(ws[2].value))
    for i in range(1, max_row):
        row = ws[i]
        # print("sheetvalue:" + str(ws.rows(i)))
        itemName = row[1]
        Specs = row[2]
        Brand = row[3]
        Unit = row[4]
        Count = row[5]
        Tax = 0
        add_date = d1
        up_date = d1
        record = ProjectItem.objects.create(projectId=projectId,
                                            itemName=itemName,
                                            Specs=Specs,
                                            Brand=Brand,
                                            Unit=Unit,
                                            Count=Count,
                                            Tax=Tax,
                                            add_date=add_date,
                                            up_date=up_date)
        print("插入明细:" + itemName + ",ID：" + str(record.itemID))
    return 1


# @csrf_exempt
def upload(file):
    # 根name取 file 的值
    # file = request.FILES.get('file')
    # 取日期
    d1 = timezone.now()
    f_url = settings.UPLOAD_ROOT + "/" + str(d1.year) + "/" + str(d1.month)  # upload/年份/月份
    f_ext = file.name.split(".")[-1]
    out_url = ""
    # uuid.uuid1()　　基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。
    #
    # 　　uuid.uuid2()　　算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。不过需要注意的是python中没有基于DCE的算法，所以python的uuid模块中没有uuid2这个方法。
    #
    # 　　uuid.uuid3(namespace,
    #              name)　　通过计算一个命名空间和名字的md5散列值来给出一个uuid，所以可以保证命名空间中的不同名字具有不同的uuid，但是相同的名字就是相同的uuid了。【感谢评论区大佬指出】namespace并不是一个自己手动指定的字符串或其他量，而是在uuid模块中本身给出的一些值。比如uuid.NAMESPACE_DNS，uuid.NAMESPACE_OID，uuid.NAMESPACE_OID这些值。这些值本身也是UUID对象，根据一定的规则计算得出。
    #
    # 　　uuid.uuid4()　　通过伪随机数得到uuid，是有一定概率重复的
    #
    # 　　uuid.uuid5(namespace, name)　　和uuid3基本相同，只不过采用的散列算法是sha1

    # f_name = "xwl" + str(d1.year) + str(d1.month) + str(d1.day) + str(d1.second) + str(d1.microsecond)
    f_name = "xwl" + str(uuid.uuid1())
    print('f_url:%s' % f_url)
    print('uplaod:%s' % file)
    print('f_name:%s' % f_name)
    print('f_ext:%s' % f_ext)
    # ip = request.META['REMOTE_ADDR']
    ip = ""
    print('ip:%s' % ip)
    # 创建upload文件夹
    if not os.path.exists(f_url):
        os.makedirs(f_url)
    try:
        if file is None:
            return HttpResponse('请选择要上传的文件')
        print(f_url + "/" + file.name)
        # 循环二进制写入
        with open(f_url + "/" + f_name + "." + f_ext, 'wb') as f:
            for i in file.readlines():
                f.write(i)
        f_size = os.path.getsize(f_url + "/" + f_name + "." + f_ext)
        out_url = "/" + str(d1.year) + "/" + str(d1.month) + "/" + f_name + "." + f_ext
        # 附件参数写入 mysql
        record = Att.objects.create(TypeID=0,
                                    ParentID=0,
                                    FileUrl=out_url,
                                    Ext=f_ext,
                                    UserID=0,
                                    UserName="",
                                    Des=file.name,
                                    Tag="",
                                    Size=f_size,
                                    Ip=ip)
        print('附件信息写入数据库:' + record.Des)

        # 表格明细写入 mysql
        # wrdb(file.name)
    except Exception as e:
        return HttpResponse(e)

    # return HttpResponse('导入成功')
    # return HttpResponse(out_url)
    return out_url


def file_down(request):
    f = Att.objects.get(AttID=request.GET.get('attid'))
    file = open(settings.UPLOAD_ROOT + f.FileUrl, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + f.FileUrl
    print('附件信息:' + f.Des)
    return response
