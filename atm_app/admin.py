from django.contrib import admin

from . models import Transaction
# Register your models here.

@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = [
        'amount_to_withdraw',
        'amount_to_deposit',
        'check_balance',
        'user'
    ]