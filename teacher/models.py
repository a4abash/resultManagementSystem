from django.db import models
from account.models import Account
from student.models import Student
# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name