from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from students.models import Student
from .models import WorkoutSheet, WorkoutDay
from .forms import WorkoutDayForm
from django.contrib import messages
from icecream import ic
from .utils import (
    get_student_id_from_session,
    student_has_training_sheet,
    get_training_sheet_or_none,
    add_training_sheet_to_session,  
    )


def training_sheet_list_view(request):
    student = get_object_or_404(
        Student,
        id=get_student_id_from_session(request)
        )
    context = {
        "student": student,
    }

    if student_has_training_sheet(student):
        training_sheets = get_list_or_404(student.trainings.all())
        context['training_sheets'] = training_sheets

    return render(request, 'training_sheet_list.html', context=context)


def create_new_training_sheet(request):
    student = get_object_or_404(Student, id=get_student_id_from_session(request))
    training_sheet = WorkoutSheet.objects.create(
        student=student,
    )
    return redirect('training_sheet_detail', training_sheet.pk)


def training_sheet_detail_view(request, sheet_id):
    training_sheet = get_object_or_404(WorkoutSheet, id=sheet_id)
    student = training_sheet.student
    training_days = training_sheet.days.all()

    context = {
        "sheet": training_sheet,
        "student": student,
        "training_days": training_days,

    }
    ic(context)
    return render(request, 'training_sheet_detail.html', context)


def training_sheet_delete_view(request, sheet_id):
    training_sheet = get_object_or_404(WorkoutSheet, id=sheet_id)
    if request.method == 'POST':
        training_sheet = get_object_or_404(WorkoutSheet, id=sheet_id)
        training_sheet.delete()
        messages.success(request, 'Ficha de Treino excluída com sucesso.')
        return redirect('training_sheet_list')

    context = {
        "training_sheet": training_sheet,
        "student": training_sheet.student
    }
    return render(request, 'training_sheet_delete.html', context)


def training_sheet_day_add_view(request, sheet_id):
    training_sheet = get_object_or_404(WorkoutSheet, id=sheet_id)
    student = training_sheet.student
    training_days = training_sheet.days.all()


    form = WorkoutDayForm()
    if request.method == 'POST':
        for day in training_days:
            if request.POST['week_day'] == day.week_day:
                messages.warning(request, f'{day} já existe na ficha deste aluno, adicione outro dia ou retorne')
                return redirect('training_sheet_day_add', training_sheet.pk)
        form = WorkoutDayForm(request.POST)
        if form.is_valid():
            new_day = form.save(commit=False)
            new_day.workout_sheet = training_sheet
            new_day.save()
            messages.success(request, f'{new_day} adicionado(a) com sucesso.')
            return redirect('training_sheet_day_add', training_sheet.pk)
    context = {
        "sheet": training_sheet,
        "student": student,
        "training_days": training_days,
        "form": form,

    }
    return render(request, 'training_sheet_day_add.html', context)


def training_sheet_day_delete_view(request, sheet_day):
    day = get_object_or_404(WorkoutDay, id=sheet_day)
    day.delete()
    return redirect('training_sheet_detail', day.workout_sheet.pk)



def training_sheet_day_exercise_add(request, sheet_day):
    pass