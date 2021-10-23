from django.contrib import admin
from .models import Student,Teacher,Manager
from teacher.models import Activity

# Register your models here.

class StudentManager(admin.ModelAdmin):
    list_display = ['id','name','number','password','person','age','sex','telephone','location','describe','colleage',
                    'study_class','updated_time','created_time','link_teacher']
    list_display_links = ['id','name','number','password','person','age','sex','telephone','location','describe','colleage',
                    'study_class','updated_time','created_time','link_teacher']

class TeacherManager(admin.ModelAdmin):
    list_display = ['id','name','number','password','person','age','sex','telephone','colleage','updated_time','created_time']
    list_display_links = ['id','name','number','password','person','age','sex','telephone','colleage','updated_time','created_time']

class ManagerManager(admin.ModelAdmin):
    list_display = ['id','number','password']
    list_display_links = ['id','number','password']

admin.site.register(Student,StudentManager)
admin.site.register(Teacher,TeacherManager)
admin.site.register(Manager,ManagerManager)
