from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.models import Account
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == 'GET':
        return redirect('home')
    else:
        u = request.POST.get('email')
        p = request.POST['password']
        user = authenticate(email=u, password=p)
        if user is not None:
            login(request, user)
            if request.user.is_manager:
                return redirect('managerDash')
            elif request.user.is_teacher:
                return redirect('teacherDash')
            elif request.user.is_student:
                return redirect('studentDash')
            else:
                pass
        else:
            messages.error(request, 'Enter the valid username and password')
            return redirect('home')


def changepassword(request):
    if request.method == 'GET':
        return render(request, 'changepassword.html')
    else:
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            user = Account.objects.get(id=request.user.id)
            user.password = make_password(p1)
            user.is_firstLogin = False
            user.save()
            return redirect('signin')
        else:
            messages.add_message(request, messages.ERROR, 'password does not match')
            return redirect('change_password')


def signout(request):
    logout(request)
    return redirect('signin')
