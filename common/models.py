# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
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
    id = models.AutoField(db_column='projectId', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(null=True, default=0)  # 项目类型，邀请or公开
    projectName = models.CharField(max_length=254, null=True)  # 项目名称
    projectNo = models.CharField(max_length=254, null=True)  # 项目编号
    contacts = models.CharField(max_length=254, null=True)  # 联系人
    phone = models.CharField(max_length=254, null=True)  # 联系电话
    add_date = models.CharField(max_length=254, null=True)  # 添加日期
    start_date = models.CharField(max_length=254, null=True)  # 开始日期
    end_date = models.CharField(max_length=254, null=True)  # 结束日期
    state = models.IntegerField(null=True, default=0)  # 状态，0=询价中，1=比价中，2=结果公示
    notes = models.TextField(null=True)  # 备注
