import codecs

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import csv

from django.urls import reverse
from django.views import View
from user.models import Student,Teacher,Manager
# Create your views here.


def manager_index(request,number):
    number=number
    return render(request,'manager_index.html',locals())


class Student_info(View):
    def get(self, request, number):

        姓名 = request.GET.get('姓名')
        学号 = request.GET.get('学号')
        print(姓名, 学号)
        # 获取所有学生信息
        all_students = Student.objects.all()
        # 获取所有教师信息
        all_teachers = Teacher.objects.all()
        # 找到所有符合要求的学生
        good_students = []
        for student in all_students:
            if not 姓名 or 姓名 in student.name:
                if not 学号 or student.number == 学号:
                    good_students.append(student)
        good_students = good_students[:10]
        return render(request, 'manager_student.html', locals())

    def post(self, request, number):
        return HttpResponse(number)


class Teacher_info(View):
    def get(self, request, number):

        姓名 = request.GET.get('姓名')
        工号 = request.GET.get('工号')
        print(姓名, 工号)
        # 获取所有学生信息
        all_students = Student.objects.all()
        # 获取所有教师信息
        all_teachers = Teacher.objects.all()
        # 找到所有符合要求的学生
        good_teachers = []
        for teacher in all_teachers:
            if not 姓名 or 姓名 in teacher.name:
                if not 工号 or teacher.number == 工号:
                    good_teachers.append(teacher)
        good_teachers = good_teachers[:10]
        return render(request, 'manager_teacher.html', locals())

    def post(self, request, number):
        return HttpResponse(number)


def show(request):
    return HttpResponse('laohu')





def manager_change_information(request,number,student_id):
    student_id=student_id
    try:
        manager = Manager.objects.get(number=number)
        student = Student.objects.get(id=student_id)
        all_teachers =Teacher.objects.all()
    except Exception as e:
        print('---update student error is %s'%(e))
        return HttpResponse('---The student is not existed')

    if request.method=='GET':
        return render(request,'manager_change_sd_infor.html',locals())
    elif request.method == 'POST':
        telephone=request.POST['telephone']
        link_teacher= Teacher.objects.get(name = request.POST['link_teacher'])
        # 改
        student.telephone = telephone
        student.link_teacher = link_teacher
        # 保存
        student.save()
        return HttpResponseRedirect(reverse("user:m_student", args=(number,)))


def manager_change_teacher_information(request,number,teacher_id):
    teacher_id = teacher_id
    try:
        manager = Manager.objects.get(number=number)
        teacher = Teacher.objects.get(id=teacher_id)
    except Exception as e:
        print('---update teacher error is %s' % (e))
        return HttpResponse('---The teacher is not existed')

    if request.method == 'GET':
        return render(request, 'manager_change_th_infor.html', locals())
    elif request.method == 'POST':
        telephone = request.POST['telephone']
        # 改
        teacher.telephone = telephone

        # 保存
        teacher.save()
        return HttpResponseRedirect(reverse("user:m_teacher", args=(number,)))


def manager_delete_information(request,number,student_id):
    student_id=student_id
    print(student_id)
    if not student_id:
        return HttpResponse('---请求异常')
    try:
        student = Student.objects.get(id=student_id)
    except Exception as e:
        print('----delete student get error %s' % (e))
        return HttpResponse('---The student id is error')
    # 将其is_active改为false
    student.delete()
    # 302跳转至manager_student
    return HttpResponseRedirect(reverse("user:m_student", args=(number,)))

def manager_delete_teacher_information(request,number,teacher_id):
    teacher_id = teacher_id
    print(teacher_id)
    if not teacher_id:
        return HttpResponse('---请求异常')
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Exception as e:
        print('----delete teacher get error %s' % (e))
        return HttpResponse('---The teacher id is error')
    # 将其删除
    teacher.delete()
    # 302跳转至manager_student
    return HttpResponseRedirect(reverse("user:m_teacher", args=(number,)))


def make_sd_csv_view(request,number):
    # 告诉浏览器该文档是csv文件，而不是html
    response = HttpResponse(content_type='text/csv')
    # 浏览器用于开启，”另存为“...对话框
    response['Content-Disposition'] = 'attachment; filename="student_informantion.csv"'
    all_students=Student.objects.all()
    # csv的响应的编码格式声明
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(['id','number','name','job','password','age','sex','colleage','study_class','telephone'
                     ,'person','location','describe','created_time','updated_time','link_teacher'])
    for student in all_students:
        writer.writerow([student.id,student.number,student.name,student.job,student.password,student.age,student.sex,student.colleage,
                         student.study_class,student.telephone,student.person,student.location,student.describe,
                         student.created_time,student.updated_time,student.link_teacher])
    return response


def make_th_csv_view(request,number):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teacher_informantion.csv"'
    all_teachers = Teacher.objects.all()
    # csv的响应的编码格式声明
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(['id','number','name', 'job', 'age','password','sex', 'colleage','telephone', 'person', 'created_time', 'updated_time'])
    for teacher in all_teachers:
        writer.writerow([teacher.id, teacher.number,teacher.name, teacher.job,teacher.age,teacher.password,teacher.sex, teacher.colleage,
                        teacher.telephone, teacher.person, teacher.created_time, teacher.updated_time])
    return response