# Generated by Django 3.2.11 on 2022-03-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Att',
            fields=[
                ('AttID', models.AutoField(db_column='AttID', primary_key=True, serialize=False)),
                ('TypeID', models.IntegerField(default=0, null=True)),
                ('ParentID', models.IntegerField(default=0, null=True)),
                ('FileUrl', models.CharField(max_length=254, null=True)),
                ('Ext', models.CharField(max_length=254, null=True)),
                ('UserID', models.IntegerField(default=0, null=True)),
                ('UserName', models.CharField(max_length=254, null=True)),
                ('Des', models.CharField(max_length=254, null=True)),
                ('Tag', models.CharField(max_length=254, null=True)),
                ('Size', models.IntegerField(default=0, null=True)),
                ('Ip', models.CharField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyId', models.AutoField(db_column='companyId', primary_key=True, serialize=False)),
                ('userId', models.IntegerField(default=0, null=True)),
                ('email', models.CharField(max_length=254, null=True)),
                ('companyName', models.CharField(max_length=254, null=True)),
                ('code', models.CharField(max_length=254, null=True)),
                ('charge', models.CharField(max_length=254, null=True)),
                ('contacts', models.CharField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=254, null=True)),
                ('tel', models.CharField(max_length=254, null=True)),
                ('start_date', models.CharField(max_length=254, null=True)),
                ('end_date', models.CharField(max_length=254, null=True)),
                ('address', models.CharField(max_length=254, null=True)),
                ('range', models.CharField(max_length=254, null=True)),
                ('capital', models.CharField(max_length=254, null=True)),
                ('is_luck', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('itemID', models.AutoField(db_column='itemID', primary_key=True, serialize=False)),
                ('companyId', models.IntegerField(default=0, null=True)),
                ('itemType', models.IntegerField(default=0, null=True)),
                ('itemName', models.CharField(default=0, max_length=254)),
                ('Unit', models.CharField(default=0, max_length=254)),
                ('Specs', models.CharField(max_length=254, null=True)),
                ('Brand', models.CharField(max_length=254, null=True)),
                ('Total', models.DecimalField(decimal_places=4, default=0, max_digits=4, null=True)),
                ('Notes', models.TextField(null=True)),
                ('add_date', models.DateTimeField(max_length=254, null=True)),
                ('up_date', models.DateTimeField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(db_column='orderID', primary_key=True, serialize=False)),
                ('projectId', models.IntegerField(default=0, null=True)),
                ('userId', models.IntegerField(default=0, null=True)),
                ('userName', models.CharField(max_length=254, null=True)),
                ('totalSum', models.DecimalField(decimal_places=4, default=0, max_digits=4, null=True)),
                ('Tax', models.IntegerField(default=0, null=True)),
                ('total', models.DecimalField(decimal_places=4, default=0, max_digits=4, null=True)),
                ('contacts', models.CharField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=254, null=True)),
                ('add_date', models.DateTimeField(max_length=254, null=True)),
                ('up_date', models.DateTimeField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderCompany',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('companyCode', models.CharField(max_length=254, null=True)),
                ('companyName', models.CharField(max_length=254, null=True)),
                ('projectId', models.IntegerField(default=0, null=True)),
                ('state', models.IntegerField(default=0, null=True)),
                ('up_date', models.DateTimeField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('itemID', models.AutoField(db_column='itemID', primary_key=True, serialize=False)),
                ('orderId', models.IntegerField(default=0, null=True)),
                ('itemName', models.CharField(default=0, max_length=254)),
                ('Count', models.IntegerField(default=0, null=True)),
                ('Unit', models.CharField(default=0, max_length=254)),
                ('Specs', models.CharField(max_length=254, null=True)),
                ('Brand', models.CharField(max_length=254, null=True)),
                ('total', models.DecimalField(decimal_places=4, default=0, max_digits=4, null=True)),
                ('totalSum', models.DecimalField(decimal_places=4, default=0, max_digits=4, null=True)),
                ('add_date', models.DateTimeField(max_length=254, null=True)),
                ('up_date', models.DateTimeField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectId', models.AutoField(db_column='projectId', primary_key=True, serialize=False)),
                ('type', models.IntegerField(default=0, null=True)),
                ('projectName', models.CharField(max_length=254, null=True)),
                ('projectNo', models.CharField(max_length=254, null=True)),
                ('contacts', models.CharField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=254, null=True)),
                ('add_date', models.DateTimeField(max_length=254, null=True)),
                ('start_date', models.DateTimeField(max_length=254, null=True)),
                ('end_date', models.DateTimeField(max_length=254, null=True)),
                ('state', models.IntegerField(default=0, null=True)),
                ('Tax', models.IntegerField(default=0, null=True)),
                ('notes', models.TextField(null=True)),
                ('up_date', models.DateTimeField(max_length=254, null=True)),
                ('arrivalTime', models.DateTimeField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('itemID', models.AutoField(db_column='itemID', primary_key=True, serialize=False)),
                ('projectId', models.IntegerField(default=0, null=True)),
                ('itemName', models.CharField(max_length=254, null=True)),
                ('Count', models.IntegerField(default=0, null=True)),
                ('Unit', models.CharField(default=0, max_length=254)),
                ('Specs', models.CharField(max_length=254, null=True)),
                ('Brand', models.CharField(max_length=254, null=True)),
                ('Tax', models.IntegerField(default=0, null=True)),
                ('add_date', models.DateTimeField(max_length=254, null=True)),
                ('up_date', models.DateTimeField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unitID', models.AutoField(db_column='unitID', primary_key=True, serialize=False)),
                ('unitName', models.CharField(default=0, max_length=254)),
            ],
        ),
    ]