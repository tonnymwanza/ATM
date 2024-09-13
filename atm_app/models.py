from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transaction(models.Model):
    amount_to_withdraw = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    amount_to_deposit = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    check_balance = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)