from django.shortcuts import render, redirect
from students.models import Student
from payments.models import Payment, PaymentValue, PaymentMethod
from django.db import models
from datetime import datetime, timedelta
from icecream import ic
from django.utils import timezone


def homepage(request):
    if 'default_date' in request.session:
        default_date = datetime.strptime(request.session['default_date'], '%Y-%m-%d').date()
    else:
        default_date = datetime.today().date()

    context = {}
    total_value_by_method = {
        "PIX": 0,
        "DINHEIRO": 0,
        "CARTÃO": 0
    }

    payments = Payment.objects.filter(payment_date=default_date)
    payments_total_sum = 0

    if request.method == "POST":
        input_date_str = request.POST.get('date', '')
        if input_date_str:
            try:
                input_date_formatted = datetime.strptime(input_date_str, '%Y-%m-%d').date()
                payments = Payment.objects.filter(payment_date=input_date_formatted)
                request.session['default_date'] = str(input_date_formatted)
                return redirect('homepage')
            except ValueError:
                pass

        if 'daily_payments' in request.POST:
            payments = Payment.objects.filter(payment_date=default_date)
            context['button_day'] = 'primary'
            context['button_month'] = 'secondary'

        elif 'monthly_payments' in request.POST:
            payments = Payment.objects.filter(
                payment_date__month=default_date.month,
                payment_date__year=default_date.year
            )
            context['button_day'] = 'secondary'
            context['button_month'] = 'primary'



    for payment in payments:
        for value in payment.values.all():
            total_value_by_method[f"{value.method}"] += value.value
        payments_total_sum += sum(value.value for value in payment.values.all())        

    payments_quantity = payments.count()
    payment_methods = PaymentMethod.objects.all()

    context['total_value_by_method'] = total_value_by_method
    context['payments'] = payments.order_by('payment_date')
    context['payments_quantity'] = payments_quantity
    context['payments_total_sum'] = payments_total_sum
    context['current_date'] = default_date

    return render(request, 'homepage.html', context)
