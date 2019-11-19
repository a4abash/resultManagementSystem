from django.db import models
from account.models import Account


class Manager(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name