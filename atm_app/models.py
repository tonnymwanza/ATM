from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Withdraw(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Balance(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)