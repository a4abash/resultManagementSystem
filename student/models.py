from django.db import models
from account.models import Account
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Result(models.Model):
    rts = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    se = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    compiler = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    webtech = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    imgprcss = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return Student.name