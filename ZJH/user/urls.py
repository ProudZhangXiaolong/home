from django.urls import path,include
from user import urls as user_urls
from user import views as user_views
from  student import views as student_views
from  teacher import views as teacher_views
from  manager import views as manager_views

from django.conf import settings
from django.conf.urls.static import static

app_name="user"

urlpatterns = [
    path('sign', user_views.sign_view,name="sign"),
    path('login',user_views.login_view,name="login"),

    path('student/<int:number>',student_views.student_index,name="student"),
    path('student/<int:number>/scanf_information',student_views.student_scanf_information,name="scanf"),
    path('student/<int:number>/change_information',student_views.student_change_information,name="change"),

    path('teacher/<int:number>', teacher_views.teacher_index, name="teacher"),
    path('teacher/<int:number>/scanf_information',teacher_views.teacher_scanf_information,name="t_scanf"),
    path('teacher/<int:number>/change_information', teacher_views.teacher_change_information, name="t_change"),
    path('teacher/<int:number>/login_active', teacher_views.teacher_login_active, name="t_login"),
    path('teacher/<int:number>/scanf_activity', teacher_views.teacher_scanf_active, name="t_scanf_active"),
    path('teacher/<int:number>/delete_activity/<int:activity_id>', teacher_views.teacher_activity_delete, name="t_delete_active"),

    path('manager/<int:number>', manager_views.manager_index, name="manager"),
    path('manager/<int:number>/student_information', manager_views.Student_info.as_view(), name="m_student"),
    path('manager/<int:number>/teacher_information', manager_views.Teacher_info.as_view(), name="m_teacher"),

    path('manager/<int:number>/change_student_information/<int:student_id>', manager_views.manager_change_information, name="m_student_change"),
    path('manager/<int:number>/delete_student_information/<int:student_id>', manager_views.manager_delete_information, name="m_student_delete"),

    path('manager/<int:number>/change_teacher_information/<int:teacher_id>', manager_views.manager_change_teacher_information,
         name="m_teacher_change"),
    path('manager/<int:number>/delete_teacher_information/<int:teacher_id>', manager_views.manager_delete_teacher_information,
         name="m_teacher_delete"),

    path('manager/<int:number>/download_student_information', manager_views.make_sd_csv_view, name="m_sd_download"),
    path('manager/<int:number>/download_teacher_information', manager_views.make_th_csv_view, name="m_th_download"),
    path('manager/<int:number>/download_teacher_information', manager_views.make_th_csv_view, name="m_th_download"),

]