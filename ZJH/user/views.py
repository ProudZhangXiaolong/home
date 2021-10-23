from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Student,Teacher,Manager

# Create your views here.
def logout(request):
    request.session.clear()
    return redirect('/')

def sign_view(request):
    # 注册
    if request.method == 'GET':
        # GET 返回页面
        return render(request, 'sign.html')
    elif request.method == 'POST':
        number = request.POST['number']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        job = request.POST.get('job',None)

        if job =="学生":
            print(job)
            if password_1 != password_2:
                return HttpResponse('两次密码输入不一致')
            #  2.当前用户名是否可用
            old_users = Student.objects.filter(number=number)
            print(old_users)
            if old_users:
                return HttpResponse('用户名已注册')
            #  3.插入数据
            # 有唯一索引的时候 try
            try:
                student = Student.objects.create(number=number, password=password_1)
            except Exception as e:
                # 有可能报错-重复插入[唯一索引并发写入问题]
                print('--create student error %s' % (e))
                return HttpResponse('用户名已注册')

            return HttpResponseRedirect(reverse("user:login",args=()))

        if job =="教师":
            print(job)
            if password_1 != password_2:
                return HttpResponse('两次密码输入不一致')
            #  2.当前用户名是否可用
            old_users = Teacher.objects.filter(number=number)
            print(old_users)
            if old_users:
                return HttpResponse('用户名已注册')
            #  3.插入数据
            # 有唯一索引的时候 try
            try:
                teacher = Teacher.objects.create(number=number, password=password_1)
            except Exception as e:
                # 有可能报错-重复插入[唯一索引并发写入问题]
                print('--create teacher error %s' % (e))
                return HttpResponse('用户名已注册')

            return HttpResponseRedirect(reverse("user:login", args=()))

        if job =="员工":
            print(job)
            if password_1 != password_2:
                return HttpResponse('两次密码输入不一致')
            #  2.当前用户名是否可用
            old_users = Manager.objects.filter(number=number)
            print(old_users)
            if old_users:
                return HttpResponse('用户名已注册')
            #  3.插入数据
            # 有唯一索引的时候 try
            try:
                manager = Manager.objects.create(number=number, password=password_1)
            except Exception as e:
                # 有可能报错-重复插入[唯一索引并发写入问题]
                print('--create manager error %s' % (e))
                return HttpResponse('用户名已注册')

            return HttpResponseRedirect(reverse("user:login", args=()))

def login_view(request):
    if request.method=='GET':
        username = request.session.get('username')

        print(username)
        if username:
            remap = {'学生': 'student', '教师': 'teacher', '员工': 'manager'}
            job = remap[request.session.get('job')]
            return redirect(f'user/{job}/{username}')
        else:
            return render(request, 'login.html')

    elif request.method=='POST':
        # 处理数据
        number=request.POST['number']
        password=request.POST['password']
        job = request.POST.get('job', None)

        if job == "学生":
            try:
                student = Student.objects.get(number=number)
            except Exception as e:
                print('--login user error %s' % (e))
                return HttpResponse('用户名或密码错误')

            if password!= student.password:
                return HttpResponse('用户名或密码错误')
            request.session['username'] = number
            request.session['job'] = job
            return HttpResponseRedirect(reverse('user:student',args=(number,)))

        if job == "教师":
            try:
                teacher = Teacher.objects.get(number=number)
            except Exception as e:
                print('--login user error %s' % (e))
                return HttpResponse('用户名或密码错误')

            if password!= teacher.password:
                return HttpResponse('用户名或密码错误')
            request.session['username'] = number
            request.session['job'] = job
            return HttpResponseRedirect(reverse('user:teacher',args=(number,)))

        if job == "员工":
            try:
                manager = Manager.objects.get(number=number)
            except Exception as e:
                print('--login user error %s' % (e))
                return HttpResponse('用户名或密码错误')

            if password!= manager.password:
                return HttpResponse('用户名或密码错误')

            request.session['username'] = number
            request.session['job'] = job
            return HttpResponseRedirect(reverse('user:manager',args=(number,)))



