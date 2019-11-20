from django.shortcuts import render, redirect


# Create your views here.
def teacherDash(request):
    if request.user.is_firstLogin:
        return redirect('changepass')
    else:
        return render(request, 'teacher/dashboard.html')