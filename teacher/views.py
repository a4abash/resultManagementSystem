from django.shortcuts import render, redirect
from teacher.models import Teacher
from student.models import Student, Result


# Create your views here.
def teacherDash(request):
    if request.user.is_firstLogin:
        return redirect('changepass')
    else:
        result = Result.objects.all()
        context = {
            'result': result
        }
        return render(request, 'teacher/dashboard.html', context)