from django import forms
from cadmember.models import Member, City
import re


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
                attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"
            ),
            "city_birth": forms.Select(attrs={"class": "form-select"}),
            "state_birth": forms.Select(attrs={"class": "form-select"}),
            "date_baptism": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"
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

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if cpf:
            # Remove any non-digit characters
            cpf = re.sub(r"\D", "", cpf)

            # Check if it has 11 digits
            if len(cpf) != 11:
                raise forms.ValidationError("CPF deve ter 11 dígitos.")

            # Check if all digits are the same
            if cpf == cpf[0] * 11:
                raise forms.ValidationError("CPF inválido.")

            # Validate first digit
            sum = 0
            for i in range(9):
                sum += int(cpf[i]) * (10 - i)
            digit = 11 - (sum % 11)
            if digit > 9:
                digit = 0
            if str(digit) != cpf[9]:
                raise forms.ValidationError("CPF inválido.")

            # Validate second digit
            sum = 0
            for i in range(10):
                sum += int(cpf[i]) * (11 - i)
            digit = 11 - (sum % 11)
            if digit > 9:
                digit = 0
            if str(digit) != cpf[10]:
                raise forms.ValidationError("CPF inválido.")

        return cpf

    def clean(self):
        cleaned_data = super().clean()
        # Você pode adicionar validações adicionais aqui se necessário
        return cleaned_data

    def save(self, commit=True):
        instance = super(MemberForm, self).save(commit=False)

        instance.name = self.cleaned_data["name"].upper()
        instance.address = self.cleaned_data["address"].upper()

        if commit:
            instance.save()
        return instance
