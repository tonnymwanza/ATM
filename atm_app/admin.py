from django.contrib import admin

from .models import Balance
from .models import Withdraw
from .models import Deposit
# Register your models here.

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = [
        'amount',
        # 'user'
    ]

@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = [
        'amount',
        # 'user'
    ]

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = [
        'amount',
        # 'user'
    ]