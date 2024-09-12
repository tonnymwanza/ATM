from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Deposit(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# class Withdraw(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# class Balance(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Transaction(models.Model):
    amount_to_withdraw = models.DecimalField(max_digits=6, decimal_places=2)
    amount_to_deposit = models.DecimalField(max_digits=6, decimal_places=2)
    check_balance = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)