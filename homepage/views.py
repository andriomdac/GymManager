from django.shortcuts import render
from students.models import Student
from payments.models import Payment, PaymentValue
from django.db import models
from icecream import ic

def homepage(request):
    payments = Payment.objects.all()
    payments_quantity = Payment.objects.all().count()
   
    payments_total_sum = 0
    for payment in payments:
        for value in payment.values.all():
            payments_total_sum += value.value
    
    context = {
        "payments": payments,
        "payments_quantity": payments_quantity
    }
    return render(request, 'homepage.html', context)
