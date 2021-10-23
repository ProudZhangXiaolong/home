from django.shortcuts import render
from user.models import Teacher
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Activity

# Create your views here.

def teacher_index(request,number):
    number = number
    return render(request, 'teacher_index.html', locals())


def teacher_scanf_information(request,number):
    teacher_login=Teacher.objects.get(number=number)

    # 通过student_set获取teacher_login对应的多个Student数据对象
    link_student=teacher_login.student_set.all()
    return render(request,'teacher_information.html',locals())


def teacher_change_information(request,number):
    try:
        teacher_change = Teacher.objects.get(number=number)
    except Exception as e:
        print('--update teacher error is %s'%(e))
        return HttpResponse('--The teacher is not existed')
    if request.method=='GET':
        return render(request,'teacher_information_change.html',locals())
    elif request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        age = request.POST['age']
        person = request.POST['person']
        colleage = request.POST['colleage']
        study_class = request.POST['age']
        telephone = request.POST['telephone']
        # 改
        teacher_change.name=name
        teacher_change.sex=sex
        teacher_change.age=age
        teacher_change.person=person
        teacher_change.colleage=colleage
        teacher_change.study_class=study_class
        teacher_change.telephone=telephone
        # # 保存
        teacher_change.save()
        return HttpResponseRedirect(reverse("user:t_scanf",args=(number,)))

def teacher_login_active(request,number):
    try:
        teacher_login = Teacher.objects.get(number=number)
        link_student = teacher_login.student_set.all()
    except Exception as e:
        print('--login teacher error is %s'%(e))
        return HttpResponse('--The teacher is not existed')
    if request.method=='GET':
        return render(request,'teacher_login_active.html',locals())
    elif request.method == 'POST':
        type = request.POST['type']
        title = request.POST['title']
        people = request.POST['people']
        image = request.FILES['image']
        content = request.POST['content']
        # 创建一共与之对应的活动
        teacher_login_activity = Activity.objects.create(number=teacher_login.number)
        # 改
        teacher_login_activity.type=type
        teacher_login_activity.title=title
        teacher_login_activity.people=people
        teacher_login_activity.image = image
        teacher_login_activity.content = content
        teacher_login_activity.link_teacher = teacher_login
        #  保存
        teacher_login_activity.save()
        return HttpResponseRedirect(reverse("user:t_scanf_active",args=(number,)))


def teacher_scanf_active(request,number):
    # 活动
    activity = Activity.objects.filter(number=number)
    # 教师
    teacher = Teacher.objects.get(number=number)
    return render(request, 'teacher_activity_info.html', locals())

def teacher_activity_delete(request,number,activity_id):
    # 通过查询字符串获取activity_id

    activity_id = activity_id
    print(activity_id)
    if not activity_id:
        return HttpResponse('---请求异常')
    try:
        activity = Activity.objects.get(id=activity_id)
    except Exception as e:
        print('----delete activity get error %s'%(e))
        return HttpResponse('---The activity id is error')
    # 将其is_active改为false
    activity.delete()
    # 302跳转至teacher_scanf_active
    return HttpResponseRedirect(reverse("user:t_scanf_active",args=(number,)))
