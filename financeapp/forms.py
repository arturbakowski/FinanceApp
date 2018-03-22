from django import forms
from .models import *


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ['income_name', 'amount']