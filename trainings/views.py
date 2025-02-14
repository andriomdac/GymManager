from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from students.models import Student
from .models import WorkoutSheet
from .forms import WorkoutDayForm
from django.contrib import messages
from icecream import ic


def student_has_training_sheet(student_instance):
    if student_instance.trainings.all().count() > 0:
        return True
    return False


def get_training_sheet_or_none(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if 'training_sheet_id' in request.session:
        try:
            training_sheet = WorkoutSheet.objects.get(
                student=student_id
                )
            return training_sheet
        except WorkoutSheet.DoesNotExist:
            return None
    return None
  

def training_sheet_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    training_sheets = get_list_or_404(student.trainings.all())
    context = {
        "student": student,
        "training_sheets": training_sheets
    }
    return render(request, 'training_sheet_list.html', context=context)


def training_day_add_view(request, student_id):
    training_sheet = get_training_sheet_or_none(request, student_id)
    form = WorkoutDayForm()
    if request.method == "POST":
        form = WorkoutDayForm(request.POST)
        if form.is_valid():
            workout_day = form.save(commit=False)
            workout_day.workout_sheet = training_sheet
            workout_day.save()
            return redirect('training_day_add', student_id)
        else:
            ic(f'form não válido: {form.errors}')
    context = {
        "form": form
    }
    return render(request, 'training_add.html', context=context)