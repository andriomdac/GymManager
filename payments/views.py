from django.shortcuts import render, redirect
from students.models import Student
from .models import Payment, PaymentValue
from .forms import PaymentForm, PaymentValueForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .utils import (
    add_payment_id_to_session,
    remove_payment_id_to_session,
    get_next_payment_date,
    delete_payment_from_id,
    verify_unfinished_payment,
    )


def add_value(request, student_id):

    payment = get_object_or_404(Payment, id=request.session['payment_id'])
    student = get_object_or_404(Student, id=student_id)
    payment_values = PaymentValue.objects.filter(payment=payment)
    form = PaymentValueForm()

    if request.method == "POST":
        if 'cancel_payment' in request.POST:
            delete_payment_from_id(payment.pk)
            remove_payment_id_to_session(request)
            return redirect("detail_student", student_id)
        if 'confirm_payment' in request.POST:
            messages.success(request, f'Pagamento para o aluno {student} realizado com sucesso.')
            remove_payment_id_to_session(request=request)
            return redirect("detail_student", student_id)
        if 'delete_value' in request.POST:
            payment_value_id = int(request.POST.get('payment_value_id'))
            payment_value = get_object_or_404(PaymentValue, id=payment_value_id)
            payment_value.delete()
            return redirect('add_value', student_id)

        form = PaymentValueForm(request.POST)
        if form.is_valid():
            new_value = form.save(commit=False)
            new_value.payment = payment
            new_value.save()
            return redirect('add_value', student_id)

    values_total = 0
    for payment_value in payment_values:
        values_total += payment_value.value
    
    context = {
        "form": form,
        "payment_values": payment_values,
        "values_total": values_total,
        "student": student,
        "payment": payment
        }

    return render(request, template_name="add_value.html", context=context)


def delete_value(request, student_id):
    payment_value_id = request.session['payment_value_id']
    payment_value = get_object_or_404(PaymentValue, id=payment_value_id)
    payment_value.delete()
    return redirect('add_value', student_id)


def add_payment(request, student_id):
    unfinished_payment = verify_unfinished_payment(request)
    if unfinished_payment:
        return unfinished_payment

    student = get_object_or_404(Student, id=student_id)
    payment_form = PaymentForm()
    if request.method == "POST":

        if 'cancel_payment' in request.POST:
            remove_payment_id_to_session(request)
            return redirect('detail_student', student_id)

        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            new_payment = payment_form.save(commit=False)
            new_payment.next_payment_date = get_next_payment_date(
                payment_date=new_payment.payment_date,
                payment_package=new_payment.payment_package
                )
            new_payment.student = student
            new_payment.save()
            add_payment_id_to_session(request, payment_id=new_payment.pk)
            return redirect('add_value', student_id)
        else:
            messages.error(request, 'Erro. Verifique os dados do pagamento.', extra_tags='danger')
            return redirect('add_payment', student_id)

    context = {
        "form": payment_form,
        "student": student,
        }

    return render(request, template_name="add_payment.html", context=context)


def delete_payment(request, student_id):
    payment_id = int(request.session['payment_id'])
    payment = get_object_or_404(Payment, id=payment_id)
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        payment.delete()
        messages.success(request, f'Pagamento do aluno {student.name} deletado com sucesso.')
        return redirect('detail_student', student_id)

    context = {
        "student": student,
        "payment": payment
    }
    return render(request, template_name="delete_payment.html", context=context)


def unfinished_payment(request, student_id):
    payment = get_object_or_404(Payment, id=int(request.session['payment_id']))
    student = get_object_or_404(Student, id=payment.student.pk)
    if request.method == 'POST':
        if 'go_to_payment' in request.POST:
            messages.warning(request, '''Adicione um valor ao pagamento e confirme,
             ou cancele o pagamento caso o registro não for mais necessário.''')
            return redirect('add_value', student_id)
    context = {
        "student": student
    }
    return render(request, 'unfinished_payment.html')