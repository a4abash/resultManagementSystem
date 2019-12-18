from django.shortcuts import render, redirect
from account.models import Account
from django.contrib import messages
from teacher.models import Teacher
from student.models import Student, Result
from resultmgmt.mail import Mail
from django.contrib.auth.hashers import make_password
from resultmgmt.password import getRandomPassword
from manager.forms import Addresult
# Create your views here.


def managerDash(request):
    return render(request, 'manager/dashboard.html')


def managerStd(request):
    if request.method == 'GET':
        return render(request, 'manager/stddashboard.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = getRandomPassword()
        user = Account(email=email, password=make_password(password), is_student=True, is_manager=False)
        user.save()
        msg = f'{name}, Your Account is created successfully, to log into your account \n please use \n email: {email} \n password : {password}'
        Mail(subject='Account Created', message=msg, recipient_list=[email])
        student = Student(name=name, user_id=user.id)
        student.save()
        messages.success(request, "Account created successfully please do check your email")
        return redirect('managerStd')


def managerTeach(request):
    if request.method == 'GET':
        return render(request, 'manager/teachdashboard.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = getRandomPassword()
        user = Account(email=email, password=make_password(password), is_teacher=True, is_manager=False)
        user.save()
        msg = f'{name}, Your Account is created successfully, to log into your account \n please use \n email: {email} \n password : {password}'
        Mail(subject='Account Created', message=msg, recipient_list=[email])
        teacher = Teacher(name=name, user_id=user.id)
        teacher.save()
        messages.success(request, "Account created successfully please do check your email")
        return redirect('managerTeach')


def mresult(request):
    if request.method == 'GET':
        result = Result.objects.all()[::-1]  # negative slicing
        context = {
            'mstdresult': result,
            'addresult': Addresult(),
        }
        return render(request, 'manager/mresult.html', context)
    else:
        form = Addresult(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
        return redirect('mresult')


def rmvprj(request, x):
    s = Student.objects.get(id=x)
    r = Result.objects.get(id=x)
    r.delete()
    return redirect('mresult')


def editresult(request, x):
        r = Result.objects.get(id=x)
        form = Addresult(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mresult')
        context = {
            'form': Addresult()
        }
        return render(request, 'editresult.html', context)

