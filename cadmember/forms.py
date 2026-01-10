from django import forms
from .models import Member, Contribution


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ["member", "value", "date", "type", "payment_method", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }