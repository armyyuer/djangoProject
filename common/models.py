# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Att(models.Model):
    attid = models.CharField(db_column='AttID', primary_key=True, max_length=255)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeID', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    fileurl = models.CharField(db_column='FileUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ext = models.CharField(db_column='Ext', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    corporate_name = models.CharField(max_length=254)  # 企业名称
    corporate_code = models.CharField(max_length=254)  # 统一社会信用代码
    corporate_email = models.CharField(max_length=254)  # 企业名称
    corporate_charge = models.CharField(max_length=254)  # 负责人
    corporate_contacts = models.CharField(max_length=254)  # 联系人
    corporate_phone = models.CharField(max_length=254)  # 联系电话
    corporate_tel = models.CharField(max_length=254)  # 企业电话
    corporate_start_date = models.CharField(max_length=254)  # 成立日期
    corporate_end_date = models.CharField(max_length=254)  # 营业期限至
    corporate_address = models.CharField(max_length=254)  # 地址
    corporate_range = models.CharField(max_length=254)  # 经营范围
    corporate_capital = models.CharField(max_length=254)  # 注册资本

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calendar(models.Model):
    calendarid = models.CharField(db_column='CalendarID', primary_key=True,
                                  max_length=255)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentID', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    describe = models.TextField(db_column='Describe', blank=True, null=True)  # Field name made lowercase.
    touser = models.CharField(db_column='ToUser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shareto = models.CharField(db_column='ShareTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reply = models.TextField(db_column='Reply', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    update = models.DateTimeField(db_column='Update', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calendar'


class Calendarreply(models.Model):
    calendarreplyid = models.CharField(db_column='CalendarReplyID', primary_key=True,
                                       max_length=255)  # Field name made lowercase.
    calendarid = models.CharField(db_column='CalendarID', max_length=255)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    describe = models.TextField(db_column='Describe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calendarreply'


class Concurrentpost(models.Model):
    concurrentpostid = models.CharField(db_column='ConcurrentPostID', primary_key=True,
                                        max_length=255)  # Field name made lowercase.
    postid = models.IntegerField(db_column='PostID', blank=True, null=True)  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    positionid = models.IntegerField(db_column='PositionID', blank=True, null=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'concurrentpost'


class Contacts(models.Model):
    contactsid = models.CharField(db_column='ContactsID', primary_key=True,
                                  max_length=100)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    contactsname = models.CharField(db_column='ContactsName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contacts'


class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True,
                                  max_length=255)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True)  # Field name made lowercase.
    degree = models.CharField(db_column='Degree', max_length=255, blank=True, null=True)  # Field name made lowercase.
    followuptime = models.DateTimeField(db_column='FollowUpTime', blank=True, null=True)  # Field name made lowercase.
    followupnumber = models.IntegerField(db_column='FollowUpNumber', blank=True,
                                         null=True)  # Field name made lowercase.
    followupcontent = models.TextField(db_column='FollowUpContent', blank=True, null=True)  # Field name made lowercase.
    sharetime = models.DateTimeField(db_column='ShareTime', blank=True, null=True)  # Field name made lowercase.
    lastfollowup = models.CharField(db_column='LastFollowUp', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customertype = models.CharField(db_column='CustomerType', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customertypeid = models.CharField(db_column='CustomerTypeID', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    sharetrue = models.IntegerField(db_column='ShareTrue', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Customershare(models.Model):
    customershareid = models.CharField(db_column='CustomerShareID', max_length=100)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    shareuser = models.CharField(db_column='ShareUser', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customershare'


class Deptment(models.Model):
    deptid = models.AutoField(db_column='DeptID', primary_key=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    describe = models.CharField(db_column='Describe', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    od = models.IntegerField(db_column='OD', blank=True, null=True)  # Field name made lowercase.
    master = models.CharField(db_column='Master', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deptment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Menu(models.Model):
    menuid = models.AutoField(db_column='MenuID', primary_key=True)  # Field name made lowercase.
    menuname = models.CharField(db_column='MenuName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    menupath = models.CharField(db_column='MenuPath', max_length=200, blank=True,
                                null=True)  # Field name made lowercase.
    od = models.IntegerField(db_column='OD', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='Img', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ioc = models.CharField(db_column='Ioc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class Position(models.Model):
    positionid = models.AutoField(db_column='PositionID', primary_key=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    describe = models.CharField(db_column='Describe', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    menuid = models.IntegerField(db_column='MenuID', blank=True, null=True)  # Field name made lowercase.
    od = models.IntegerField(db_column='OD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'position'


class Positionmenuinfo(models.Model):
    positionid = models.AutoField(db_column='PositionID', primary_key=True)  # Field name made lowercase.
    menuid = models.IntegerField(db_column='MenuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'positionmenuinfo'
        unique_together = (('positionid', 'menuid'),)


class Post(models.Model):
    postid = models.AutoField(db_column='PostID', primary_key=True)  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    describe = models.TextField(db_column='Describe', blank=True, null=True)  # Field name made lowercase.
    od = models.IntegerField(db_column='OD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'


class Project(models.Model):
    projectid = models.AutoField(db_column='ProjectID', primary_key=True)  # Field name made lowercase.
    projectnumber = models.CharField(db_column='ProjectNumber', max_length=100, blank=True,
                                     null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    plannedhours = models.IntegerField(db_column='PlannedHours', blank=True, null=True)  # Field name made lowercase.
    actualhours = models.IntegerField(db_column='ActualHours', blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeID', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    approved = models.CharField(db_column='Approved', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    founder = models.CharField(db_column='Founder', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classifyid = models.IntegerField(db_column='ClassifyID', blank=True, null=True)  # Field name made lowercase.
    classifyname = models.CharField(db_column='ClassifyName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    viewer = models.CharField(db_column='Viewer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    describe = models.CharField(db_column='Describe', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class Returnvisit(models.Model):
    returnvisitid = models.CharField(db_column='ReturnVisitID', primary_key=True,
                                     max_length=100)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    followupmode = models.CharField(db_column='FollowUpMode', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    followuptime = models.DateTimeField(db_column='FollowUpTime', blank=True, null=True)  # Field name made lowercase.
    followupcontent = models.TextField(db_column='FollowUpContent', blank=True, null=True)  # Field name made lowercase.
    followupnexttime = models.DateTimeField(db_column='FollowUpNextTime', blank=True,
                                            null=True)  # Field name made lowercase.
    remind = models.IntegerField(db_column='Remind', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'returnvisit'


class Role(models.Model):
    roleid = models.AutoField(db_column='RoleID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class Seal(models.Model):
    sealid = models.AutoField(db_column='SealID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    sealname = models.CharField(db_column='SealName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    passtrue = models.IntegerField(db_column='PassTrue', blank=True, null=True)  # Field name made lowercase.
    sealurl = models.CharField(db_column='SealUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seal'


class Syslog(models.Model):
    syslogid = models.AutoField(db_column='SysLogID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syslog'


class Task(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    tasktitle = models.CharField(db_column='TaskTitle', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    prepositionid = models.IntegerField(db_column='PrepositionID', blank=True, null=True)  # Field name made lowercase.
    preposition = models.CharField(db_column='Preposition', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    executor = models.CharField(db_column='Executor', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=255, blank=True, null=True)  # Field name made lowercase.
    milepost = models.IntegerField(db_column='Milepost', blank=True, null=True)  # Field name made lowercase.
    describe = models.TextField(db_column='Describe', blank=True, null=True)  # Field name made lowercase.
    rapexplain = models.TextField(db_column='RAPExplain', blank=True, null=True)  # Field name made lowercase.
    plannedhours = models.IntegerField(db_column='PlannedHours', blank=True, null=True)  # Field name made lowercase.
    actualhours = models.IntegerField(db_column='ActualHours', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'


class Track(models.Model):
    trackid = models.CharField(db_column='TrackID', primary_key=True, max_length=100)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    customertype = models.CharField(db_column='CustomerType', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    customertypeid = models.CharField(db_column='CustomerTypeID', max_length=100, blank=True,
                                      null=True)  # Field name made lowercase.
    degree = models.CharField(db_column='Degree', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactsname = models.CharField(db_column='ContactsName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    followupmode = models.CharField(db_column='FollowUpMode', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    followuptime = models.DateTimeField(db_column='FollowUpTime', blank=True, null=True)  # Field name made lowercase.
    followupcontent = models.TextField(db_column='FollowUpContent', blank=True, null=True)  # Field name made lowercase.
    followupresult = models.TextField(db_column='FollowUpResult', blank=True, null=True)  # Field name made lowercase.
    followupnexttime = models.DateTimeField(db_column='FollowUpNextTime', blank=True,
                                            null=True)  # Field name made lowercase.
    remind = models.IntegerField(db_column='Remind', blank=True, null=True)  # Field name made lowercase.
    cycleremind = models.IntegerField(db_column='CycleRemind', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'track'


class Useraccount(models.Model):
    accountid = models.AutoField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccount'


class Userinfo(models.Model):
    dduserid = models.CharField(db_column='DDUserid', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    postid = models.IntegerField(db_column='PostID', blank=True, null=True)  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    positionid = models.IntegerField(db_column='PositionID', blank=True, null=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=45, blank=True,
                                    null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    officetelephone = models.CharField(db_column='OfficeTelephone', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IDNumber', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    concurrentpost = models.IntegerField(db_column='ConcurrentPost', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'


class Usermenu(models.Model):
    usermenuid = models.AutoField(db_column='UserMenuID', primary_key=True)  # Field name made lowercase.
    enable = models.IntegerField(db_column='Enable', blank=True, null=True)  # Field name made lowercase.
    menus = models.TextField(db_column='Menus', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usermenu'
