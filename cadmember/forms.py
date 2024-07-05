from django import forms
from cadmember.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    def save(self, commit = True):
        instance = super(MemberForm, self).save(commit=False)

        instance.name = self.cleaned_data['name'].upper()
        instance.address = self.cleaned_data['address'].upper()
        

        if commit:
            instance.save()
        return instance
            
    