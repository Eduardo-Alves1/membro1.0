from django import forms
from cadmember.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
