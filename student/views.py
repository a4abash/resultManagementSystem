from django.shortcuts import render, redirect
from student.models import Student, Result


# Create your views here.
def studentDash(request):
    if request.user.is_firstLogin:
        return redirect('changepass')
    else:
        t = Student.objects.get(id=getCurrentlyLoginStudentId(request.user.id))
        x = Result.objects.get(id=getMarks(t.id))
        context = {
            'std': t,
            'stdresult': x
        }
        return render(request, 'student/dashboard.html', context)


def getCurrentlyLoginStudentId(id):
    t = Student.objects.get(user_id=id)
    return t.id


def getMarks(id):
    x = Result.objects.get(student_id=id)
    return x.id