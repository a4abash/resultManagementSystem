from django.urls import path
from . import views

urlpatterns = [
    path('', views.managerDash, name='managerDash'),
    path('student', views.managerStd, name='managerStd'),
    path('teacher', views.managerTeach, name='managerTeach')
]
