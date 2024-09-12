from django import forms
from . models import Transaction
# my forms

class TransactionForm(forms.Form):
    amount_to_withdraw = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'enter amount to withdraw'}))
    amount_to_deposit = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'enter amount to deposit'}))
    check_balance = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Check your balance'}))