from django import forms
from .models import Payment, PaymentValue


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            "payment_package",
            "observations",
            "payment_date",
            "next_payment_date",
            "user_signature",
            ]
        widgets = {
            "payment_package": forms.Select(attrs={"class": "form-control", "autofocus": ""}), 
            "observations": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "payment_date": forms.DateInput(
                attrs={"class": "form-control"}
            )
            }


class PaymentValueForm(forms.ModelForm):
    class Meta:
        model = PaymentValue
        fields = ["value", "method",]
        widgets = {
            "value": forms.NumberInput(attrs={"class": "form-control"}),
            "method": forms.Select(attrs={"class": "form-control", "autofocus": ""})

        }
