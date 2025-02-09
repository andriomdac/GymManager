from django.contrib import admin
from students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["name", "phone", "reference",]
    list_display = ["name", "phone", "reference",]