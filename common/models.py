# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' orders
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    companyId = models.AutoField(db_column='companyId', primary_key=True)  # Field name made lowercase.
    userId = models.IntegerField(null=True, default=0)  # 关联账号ID
    email = models.CharField(max_length=254, null=True)  # 邮件
    companyName = models.CharField(max_length=254, null=True)  # 企业名称
    code = models.CharField(max_length=254, null=True)  # 统一社会信用代码
    charge = models.CharField(max_length=254, null=True)  # 负责人
    contacts = models.CharField(max_length=254, null=True)  # 联系人
    phone = models.CharField(max_length=254, null=True)  # 联系电话
    tel = models.CharField(max_length=254, null=True)  # 企业电话
    start_date = models.CharField(max_length=254, null=True)  # 成立日期
    end_date = models.CharField(max_length=254, null=True)  # 营业期限至
    address = models.CharField(max_length=254, null=True)  # 地址
    range = models.CharField(max_length=254, null=True)  # 经营范围
    capital = models.CharField(max_length=254, null=True)  # 注册资本
    is_luck = models.IntegerField(null=True, default=0)


class Project(models.Model):
    projectId = models.AutoField(db_column=' ', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(null=True, default=0)  # 项目类型，邀请or公开
    projectName = models.CharField(max_length=254, null=True)  # 项目名称
    projectNo = models.CharField(max_length=254, null=True)  # 项目编号
    contacts = models.CharField(max_length=254, null=True)  # 联系人
    phone = models.CharField(max_length=254, null=True)  # 联系电话
    add_date = models.DateTimeField(max_length=254, null=True)  # 添加日期
    start_date = models.DateTimeField(max_length=254, null=True)  # 开始日期
    end_date = models.DateTimeField(max_length=254, null=True)  # 结束日期
    state = models.IntegerField(null=True, default=0)  # 状态，0=询价中，1=比价中，2=结果公示
    Tax = models.IntegerField(null=True, default=0)  # 税点
    notes = models.TextField(null=True)  # 备注
    up_date = models.DateTimeField(max_length=254, null=True)  # 更新日期
    arrivalTime = models.DateTimeField(max_length=254, null=True)  # 到货日期


class ProjectItem(models.Model):
    itemID = models.AutoField(db_column='itemID', primary_key=True)  #
    projectId = models.IntegerField(null=True, default=0)  # 项目ID
    itemName = models.CharField(max_length=254, null=True)  # 材料（设备）名称
    Count = models.IntegerField(null=True, default=0)  # 计数
    Unit = models.CharField(max_length=254, default=0)  # 单位
    Specs = models.CharField(max_length=254, null=True)  # 规格型号
    Brand = models.CharField(max_length=254, null=True)  # 品牌
    Tax = models.IntegerField(null=True, default=0)  # 税点
    add_date = models.DateTimeField(max_length=254, null=True)  # 添加日期
    up_date = models.DateTimeField(max_length=254, null=True)  # 更新日期


class Order(models.Model):
    orderID = models.AutoField(db_column='orderID', primary_key=True)  #
    projectId = models.IntegerField(null=True, default=0)  # 项目ID
    userId = models.IntegerField(null=True, default=0)  # 用户ID
    userName = models.CharField(max_length=254, null=True)  # 用户名称
    totalSum = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 总额
    Tax = models.IntegerField(null=True, default=0)  # 税点
    total = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 税收金额
    contacts = models.CharField(max_length=254, null=True)  # 联系人
    phone = models.CharField(max_length=254, null=True)  # 联系电话
    add_date = models.DateTimeField(max_length=254, null=True)  # 添加日期
    up_date = models.DateTimeField(max_length=254, null=True)  # 更新日期


class OrderItem(models.Model):
    itemID = models.AutoField(db_column='itemID', primary_key=True)  #
    orderId = models.IntegerField(null=True, default=0)  # 报价ID
    itemName = models.CharField(max_length=254, default=0)  # 材料（设备）名称
    Count = models.IntegerField(null=True, default=0)  # 计数
    Unit = models.CharField(max_length=254, default=0)  # 单位
    Specs = models.CharField(max_length=254, null=True)  # 规格型号
    Brand = models.CharField(max_length=254, null=True)  # 品牌
    total = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 单价
    totalSum = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 总额
    add_date = models.DateTimeField(max_length=254, null=True)  # 添加日期
    up_date = models.DateTimeField(max_length=254, null=True)  # 更新日期


class OrderCompany(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    companyCode = models.CharField(max_length=254, null=True)  # 企业统一社会信用代码
    companyName = models.CharField(max_length=254, null=True)  # 企业名称
    projectId = models.IntegerField(null=True, default=0)  # 项目ID
    state = models.IntegerField(null=True, default=0)  # 报价状态0=未报价，1=已报价
    up_date = models.DateTimeField(max_length=254, null=True)  # 更新日期


class Att(models.Model):
    AttID = models.AutoField(db_column='AttID', primary_key=True)  # Field name made lowercase.
    TypeID = models.IntegerField(null=True, default=0)  # 类型ID
    ParentID = models.IntegerField(null=True, default=0)  # 上级ID
    FileUrl = models.CharField(max_length=254, null=True)  # 文件地址
    Ext = models.CharField(max_length=254, null=True)  # 后缀
    UserID = models.IntegerField(null=True, default=0)  # 上传人ID
    UserName = models.CharField(max_length=254, null=True)  # 上传人
    Des = models.CharField(max_length=254, null=True)  #
    Tag = models.CharField(max_length=254, null=True)  # 标签
    Size = models.IntegerField(null=True, default=0)  # 大小，KB
    Ip = models.CharField(max_length=254, null=True)  # 标签


class Unit(models.Model):
    unitID = models.AutoField(db_column='unitID', primary_key=True)  #
    unitName = models.CharField(max_length=254, default=0)  # 单位名称


class Items(models.Model):
    itemID = models.AutoField(db_column='itemID', primary_key=True)  #
    companyId = models.IntegerField(null=True, default=0)  # 企业ID
    itemType = models.IntegerField(null=True, default=0)  # 类型0=系统
    itemName = models.CharField(max_length=254, default=0)  # 材料（设备）名称
    Unit = models.CharField(max_length=254, default=0)  # 单位
    Specs = models.CharField(max_length=254, null=True)  # 规格型号
    Brand = models.CharField(max_length=254, null=True)  # 品牌
    Total = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 单价
    Notes = models.TextField(null=True)  # 备注
    add_date = models.DateTimeField(max_length=254, null=True)  # 添加日期
    up_date = models.DateTimeField(max_length=254, null=True)  # 更新日期


class XCM(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  #
    userName = models.CharField(max_length=254, default=0)  # 人名
    img = models.CharField(max_length=254, default=0)  # 行程码图片
    DD = models.CharField(max_length=254, null=True)  # 钉钉信息
    add_date = models.DateTimeField(max_length=254, null=True)  # 添加日期


class DDuser(models.Model):
    DDuserID = models.AutoField(db_column='DDuserID', primary_key=True)  #
    userName = models.CharField(max_length=254, default=0)  # 人名
    dept = models.CharField(max_length=254, null=True)  # 部门
    DD = models.CharField(max_length=254, null=True)  # 钉钉信息
    tel = models.CharField(max_length=254, null=True)  # 钉钉信息


class SerProject(models.Model):
    projectID = models.AutoField(db_column='ProjectID', primary_key=True)  #
    projectName = models.CharField(max_length=254, null=True)  # 项目名称
    company = models.CharField(max_length=254, null=True)  # 所属公司名称
    contact = models.CharField(max_length=254, null=True)  # 项目联系人
    tel = models.CharField(max_length=254, null=True)  # 项目联系电话
    retentionMoney = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 质保金
    startTime = models.DateTimeField(max_length=254, null=True)  # 质保开始时间
    endTime = models.DateTimeField(max_length=254, null=True)  # 质保结束时间
    state = models.CharField(max_length=254, null=True)  # 状态,服务中----服务结束


class SerOrders(models.Model):
    orderID = models.AutoField(db_column='orderID', primary_key=True)  #
    company = models.CharField(max_length=254, null=True)  # 单位名称
    address = models.CharField(max_length=254, null=True)  # 地址
    contact = models.CharField(max_length=254, null=True)  # 联系人
    tel = models.CharField(max_length=254, null=True)  # 联系电话
    content = models.CharField(max_length=254, null=True)  # 报修内容
    hopeTime = models.CharField(max_length=254, null=True)  # 希望上门时间
    remarks = models.CharField(max_length=254, null=True)  # 保修备注
    projectID = models.IntegerField(null=True, default=0)  # 项目ID
    projectName = models.CharField(max_length=254, null=True)  # 项目名称
    agree = models.IntegerField(null=True, default=0)  # 是否同意客户维修申请
    repairerID = models.IntegerField(null=True, default=0)  # 维修人员ID
    repairerName = models.CharField(max_length=254, null=True)  # 维修人员姓名
    seedTime = models.DateTimeField(max_length=254, null=True)  # 派单日期
    goTime = models.DateTimeField(max_length=254, null=True)  # 上门日期
    endTime = models.DateTimeField(max_length=254, null=True)  # 结单日期
    workingHours = models.IntegerField(null=True, default=0)  # 维修工时
    fault = models.CharField(max_length=254, null=True)  # 故障描述
    record = models.CharField(max_length=254, null=True)  # 维修记录
    cost = models.DecimalField(max_digits=4, decimal_places=4, null=True, default=0)  # 维修费用
    confirm = models.CharField(max_length=254, null=True)  # 确认是否维修，维修、不维修
    image = models.CharField(max_length=254, null=True)  # 维修单拍照
    lc = models.IntegerField(null=True, default=0)  # 流程。0-报单，1-审核派单，-1-不派单，2-售后处理，3-正常结单
    state = models.CharField(max_length=254, null=True)  # 状态
    userID = models.IntegerField(null=True, default=0)  # 处理人ID
    userName = models.CharField(max_length=254, null=True)  # 处理人
    addTime = models.DateTimeField(max_length=254, null=True)  # 提交日期