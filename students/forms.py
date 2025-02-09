from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "phone",
            "reference"
            ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do Aluno", "autofocus": ""}), 
            "phone": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Telefone do Aluno"}),
            "reference": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "CPF, Identidade, Parentesco"}),
        }