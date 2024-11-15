from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from . validators import withdrawal_validator
# Create your models here.

class Transaction(models.Model):
    amount_to_withdraw = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    amount_to_deposit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    check_balance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    balance_after_withdrawal = models.DecimalField(max_digits=6, decimal_places=2, null=True)


# signal to create transaction object whenever a user is created
@receiver(post_save, sender=User)
def transaction_signal_fun(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(user=instance)