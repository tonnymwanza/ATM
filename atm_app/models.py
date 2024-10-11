from django.db import models
from django.contrib.auth.models import User

from . validators import withdrawal_validator
# Create your models here.

class Transaction(models.Model):
    amount_to_withdraw = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    amount_to_deposit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    check_balance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

