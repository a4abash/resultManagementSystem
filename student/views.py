from django.shortcuts import render, redirect


# Create your views here.
def studentDash(request):
    if request.user.is_firstLogin:
        return redirect('changepass')
    else:
        return render(request, 'student/dashboard.html')