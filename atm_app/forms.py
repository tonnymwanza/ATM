from django import forms
from . models import Withdraw
# my forms

class WithdrawForm(forms.Form):
    amount = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'enter amount to withdraw'}))