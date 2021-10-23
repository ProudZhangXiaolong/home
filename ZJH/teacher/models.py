from django.db import models
from user.models import Teacher
# Create your models here.

class Activity(models.Model):
    number = models.CharField("与老师对应的工号",max_length=10,null=True)
    type = models.CharField("活动类型",max_length=10,null=True)
    title = models.CharField("活动主题", max_length=10, null=True)
    people = models.CharField("活动对象",max_length=10,null=True)
    image = models.ImageField(verbose_name="上传照片",upload_to='img/',null=True,blank=True)
    content = models.TextField(blank=True,null=True, verbose_name="活动内容")
    created_time=models.DateTimeField("创建时间",auto_now_add=True)
    updated_time=models.DateTimeField("更新时间",auto_now=True)
    #发布的活动
    link_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="活动关联的老师", null=True)

    class Meta:
        verbose_name="三二一活动"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '%s_%s_%s_%s_%s_%s_%s'%(self.type,self.title,self.people,self.image,self.content,self.created_time,self.updated_time)
