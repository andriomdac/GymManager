from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('students/', include('students.urls')),
    path('students/<int:student_id>/', include('payments.urls')),
    path('training_sheets/', include('trainings.urls')),
]
