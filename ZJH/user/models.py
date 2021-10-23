from django.db import models

# Create your models here.

class Teacher(models.Model):
    number=models.CharField("工号",max_length=10,unique=True)
    name=models.CharField("姓名",max_length=10,null=True)
    job=models.CharField("职位",max_length=10,default='教师')
    age=models.CharField("年龄",max_length=5,null=True)
    password=models.CharField("密码",max_length=32)
    sex=models.CharField("性别",max_length=5,null=True)
    colleage=models.CharField("学院",max_length=15,null=True)
    telephone=models.CharField("电话",max_length=15,null=True)
    person = models.CharField("民族",max_length=8,null=True)
    created_time=models.DateTimeField("创建时间",auto_now_add=True)
    updated_time=models.DateTimeField("更新时间",auto_now=True)

    class Meta:
        verbose_name="教师"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '%s_%s_%s_%s_%s_%s_%s_%s_%s_%s'%(self.number,self.name,self.job,self.age,
        self.sex,self.colleage,self.telephone,self.person,self.created_time,self.updated_time)

class Student(models.Model):
    number=models.CharField("学号",max_length=10,unique=True)
    name=models.CharField("姓名",max_length=10,null=True)
    job=models.CharField("职位",max_length=10,default='学生')
    age=models.CharField("年龄",max_length=5,null=True)
    password=models.CharField("密码",max_length=32)
    sex=models.CharField("性别",max_length=5,null=True)
    colleage=models.CharField("学院",max_length=15,null=True)
    study_class=models.CharField("班级",max_length=15,null=True)
    telephone=models.CharField("电话",max_length=15,null=True)
    person = models.CharField("民族",max_length=8,null=True)
    location = models.CharField("家庭住址",max_length=50,null=True)
    link_teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="关联教师",null=True)
    describe=models.TextField(blank=True,null=True,verbose_name="自我评价")
    created_time=models.DateTimeField("创建时间",auto_now_add=True)
    updated_time=models.DateTimeField("更新时间",auto_now=True)

    class Meta:
        verbose_name="学生"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '%s_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s'%(self.number,self.name,self.job,self.age,self.study_class,
        self.sex,self.colleage,self.telephone,self.person,self.location,self.describe,self.link_teacher,self.created_time,self.updated_time)


class Manager(models.Model):
    number=models.CharField("工号",max_length=10,unique=True)
    password = models.CharField("密码", max_length=32)
    job=models.CharField("职位",max_length=10,default='员工')

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s_%s'%(self.number,self.password,self.job)
