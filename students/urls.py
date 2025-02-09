from django.urls import path
from .views import (
    list_students,
    add_student,
    update_student,
    delete_student,
    detail_student
    )

urlpatterns = [
    path('', list_students, name='list_students'),
    path('<int:student_id>/', detail_student, name='detail_student'),
    path('add/', add_student, name='add_student'),
    path('update/<int:student_id>/', update_student, name='update_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    
]