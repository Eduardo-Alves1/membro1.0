from django import forms
from cadmember.models import Member, City


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    # "pattern": "[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}",
                    "placeholder": "000.000.000-00",
                }
            ),
            "date_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "city_birth": forms.Select(attrs={"class": "form-select"}),
            "state_birth": forms.Select(attrs={"class": "form-select"}),
            "date_baptism": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": "[0-9]{5}-[0-9]{3 }",
                    "placeholder": "00000-000",
                }
            ),
        }
        labels = {
            "name": "NOME",
            "cpf": "CPF",
            "date_birth": "DATA DE NASCIMENTO",
            "city_birth": "CIDADE DE NASCIMENTO",
            "state_birth": "ESTADO DE NASCIMENTO",
            "address": "ENDEREÇO",
            "cep": "CEP",
            "date_baptism": "DATA DO BATISMO",
        }

    def save(self, commit=True):
        instance = super(MemberForm, self).save(commit=False)

        instance.name = self.cleaned_data["name"].upper()
        instance.address = self.cleaned_data["address"].upper()

        if commit:
            instance.save()
        return instance
