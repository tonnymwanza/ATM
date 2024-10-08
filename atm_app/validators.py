from django.core.exceptions import ValidationError
from django import forms

# my validators

def withdrawal_validator(value):
    value = int(value)
    if value < 50:
        raise forms.ValidationError('amount to low to be withdrawn')