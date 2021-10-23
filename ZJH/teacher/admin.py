from django.contrib import admin
from .models import Activity
# Register your models here.

class ActivityManager(admin.ModelAdmin):
    # 显示字段
    list_display = ['content','image','type','title','number','people','link_teacher','created_time','updated_time']
    # 链接到修改页面
    list_display_links = ['content','image','type','title','number','people','link_teacher','created_time','updated_time']
    list_filter = ['people']

admin.site.register(Activity,ActivityManager)
