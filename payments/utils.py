from dateutil.relativedelta import relativedelta
from payments.models import Payment
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from students.models import Student


def add_payment_id_to_session(request, payment_id):
    request.session['payment_id'] = payment_id


def remove_payment_id_to_session(request):
    if 'payment_id' in request.session:
        del request.session['payment_id']


def get_next_payment_date(payment_date, payment_package):
    '''
    Handles the number of days between the payment date and the next payment date
    based on the payment package provided.
    '''

    package = payment_package.package
    package_days = {
        "MENSAL": 31,
        "BIMESTRAL": 62,
        "TRIMESTRAL": 93,
        "SEMESTRAL": 186,
        "ANUAL": 372,
    }
    next_payment = payment_date + relativedelta(days=package_days[package])
    return next_payment


def delete_payment_from_id(payment_id):
    payment = get_object_or_404(Payment, id=payment_id).delete()


def verify_unfinished_payment(request):
    if 'payment_id' in request.session:
        try:
            payment = Payment.objects.get(id=int(request.session['payment_id']))
            return redirect('unfinished_payment', payment.student.pk)

        except Payment.DoesNotExist:
            remove_payment_id_to_session(request)
            return redirect('list_students')
    return None


def turn_payment_into_active_or_not(request, student_id):
    '''
    A payment is active if the next payment date is not achived yet by today.
    A payment is not active otherwise.
    '''
    from django.utils import timezone

    for payment in Payment.objects.filter(student=student_id):
        if payment.next_payment_date > timezone.localdate():
            payment.active = True
        else:
            payment.active = False
        payment.save()
