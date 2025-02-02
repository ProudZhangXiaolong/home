# Generated by Django 3.2.4 on 2021-06-21 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='工号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='姓名')),
                ('job', models.CharField(default='员工', max_length=10, verbose_name='职位')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='工号')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='姓名')),
                ('job', models.CharField(default='教师', max_length=10, verbose_name='职位')),
                ('age', models.CharField(max_length=5, null=True, verbose_name='年龄')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('sex', models.CharField(max_length=5, null=True, verbose_name='性别')),
                ('colleage', models.CharField(max_length=15, null=True, verbose_name='学院')),
                ('telephone', models.CharField(max_length=15, null=True, verbose_name='电话')),
                ('person', models.CharField(max_length=8, null=True, verbose_name='民族')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='学号')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='姓名')),
                ('job', models.CharField(default='学生', max_length=10, verbose_name='职位')),
                ('age', models.CharField(max_length=5, null=True, verbose_name='年龄')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('sex', models.CharField(max_length=5, null=True, verbose_name='性别')),
                ('colleage', models.CharField(max_length=15, null=True, verbose_name='学院')),
                ('study_class', models.CharField(max_length=15, null=True, verbose_name='班级')),
                ('telephone', models.CharField(max_length=15, null=True, verbose_name='电话')),
                ('person', models.CharField(max_length=8, null=True, verbose_name='民族')),
                ('location', models.CharField(max_length=50, null=True, verbose_name='家庭住址')),
                ('describe', models.TextField(blank=True, null=True, verbose_name='自我评价')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('link_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.teacher', verbose_name='关联教师')),
            ],
        ),
    ]
