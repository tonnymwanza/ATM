from django import forms
from . validators import withdrawal_validator
# my forms

class WithdrawForm(forms.Form):
    amount_to_withdraw = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'enter amount to withdraw'}))

class DepositForm(forms.Form):
    amount_to_deposit = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'enter amount to deposit'}))


class BalanceForm(forms.Form):
    check_balance = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Check your balance'}))