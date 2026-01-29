from django import forms
from .models import Contribution, Expense


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ["member", "value", "date", "type", "payment_method", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["description", "category", "value", "date", "payment_method", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
