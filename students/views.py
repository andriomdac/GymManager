from django.shortcuts import render, redirect
from .models import Student
from django.shortcuts import get_object_or_404
from .forms import StudentForm
from django.contrib import messages
from payments.models import Payment, PaymentValue
from payments.utils import verify_unfinished_payment


def list_students(request):
    unfinished_payment = verify_unfinished_payment(request)
    if unfinished_payment:
        return unfinished_payment

    students = Student.objects.all()
    search = request.POST.get("search", "")
    if search:
        students = Student.objects.filter(name__contains=search)
    context={
        "students": students,
        }
    return render(request, template_name='list_students.html', context=context)


def add_student(request):
    add_student_form = StudentForm(request.POST)
    if request.method == "POST":
        if add_student_form.is_valid():
            new_student = add_student_form.save(commit=False)
            new_student.name = new_student.name.upper()
            new_student.save()
            messages.success(request, f"Aluno {new_student.name} matriculado com sucesso.")
            return redirect(to="detail_student", student_id=new_student.pk)
        else:
            messages.error(request, 'Erro ao matricular, verifique os dados do aluno', extra_tags="danger")
    context = {
        "form": add_student_form
    }
    return render(request, template_name='add_student.html', context=context)


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    update_student_form = StudentForm(instance=student)
    if request.method == "POST":
        update_student_form = StudentForm(request.POST, instance=student)
        if update_student_form.is_valid():
            updated_student = update_student_form.save(commit=False)
            updated_student.name = updated_student.name.upper()
            updated_student.save()
            messages.success(request, f"Aluno {updated_student.name} alterado com sucesso.")
            return redirect("detail_student", student.pk)
        else:
            messages.error(request, 'Erro ao alterar, verifique os dados do aluno')
    return render(request, template_name="update_student.html", context={"form": update_student_form, "student_id": student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, f"Aluno '{student.name}' deletado com sucesso.")
        return redirect(to='list_students')
    return render(request, template_name="delete_student.html", context={"student": student})


def detail_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    payments = Payment.objects.filter(student=student).order_by('-created_at')

    if request.method == "POST":
        if 'delete_payment' in request.POST:
            request.session['payment_id'] = request.POST['payment_id']
            return redirect('delete_payment', student_id)
    context = {
        "student": student,
        "payments": payments
        }
    return render(request, template_name="detail_student.html", context=context)
