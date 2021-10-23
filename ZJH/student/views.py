from django.shortcuts import render
from user.models import Student,Teacher
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def student_index(request,number):
    number = number
    return render(request,'student_index.html',locals())

def student_scanf_information(request,number):
    student_login=Student.objects.get(number=number)
    return render(request,'student_information.html',locals())

def student_change_information(request,number):
    try:
        all_teacher = Teacher.objects.all()
        student_change = Student.objects.get(number=number)
    except Exception as e:
        print('--update student error is %s'%(e))
        return HttpResponse('--The student is not existed')
    if request.method=='GET':
        return render(request,'student_information_change.html',locals())
    elif request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        age = request.POST['age']
        person = request.POST['person']
        colleage = request.POST['colleage']
        study_class = request.POST['study_class']
        telephone = request.POST['telephone']
        location = request.POST['location']
        describe = request.POST['describe']
        link_teacher= Teacher.objects.get(name = request.POST['link_teacher'])
        # 改
        student_change.name=name
        student_change.sex=sex
        student_change.age = age
        student_change.person=person
        student_change.colleage=colleage
        student_change.study_class=study_class
        student_change.telephone=telephone
        student_change.location=location
        student_change.describe=describe
        student_change.link_teacher=link_teacher
        # 保存
        student_change.save()
        return HttpResponseRedirect(reverse("user:scanf",args=(number,)))