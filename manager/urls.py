from django.urls import path
from . import views

urlpatterns = [
    path('', views.managerDash, name='managerDash'),
    path('student', views.managerStd, name='managerStd'),
    path('teacher', views.managerTeach, name='managerTeach'),
    path('mresult',views.mresult, name='mresult'),
    path('rmvresult/<int:x>', views.rmvprj, name='rmvprj'),
    path('editresult/<int:x>', views.editresult, name='editresult'),
]
