from django import forms
from cadmember.models import Member, City


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'city_birth': forms.ModelMultipleChoiceField(queryset=City.objects.all(), widgets=forms.Select(attrs={'class': 'form-control'}))
        }
        labels = {
            'name': 'NOME',
            'cpf': 'CPF',
            # 'date_birth': 'DATA NASCIMENTO'
        }

    def save(self, commit = True):
        instance = super(MemberForm, self).save(commit=False)

        instance.name = self.cleaned_data['name'].upper()
        instance.address = self.cleaned_data['address'].upper()
        

        if commit:
            instance.save()
        return instance
            
    