from .models import WorkoutSheet


def student_has_training_sheet(student_instance):
    if student_instance.trainings.all().count() > 0:
        return True
    return False


def get_student_id_from_session(request):
    return request.session['student_id']


def get_training_sheet_or_none(request):
    student = get_student_id_from_session(request)
    if 'training_sheet_id' in request.session:
        try:
            training_sheet = WorkoutSheet.objects.get(
                student=student_id
                )
            return training_sheet
        except WorkoutSheet.DoesNotExist:
            return None
    return None



def add_training_sheet_to_session(sheet_id):
    request.session['sheet_id'] = sheet_id