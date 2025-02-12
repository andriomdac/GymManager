from django.contrib import admin
from .models import (
    WorkoutSheet,
    WorkoutDay,
    WorkoutExercice,
    WorkoutDayExercise
    )


@admin.register(WorkoutSheet)
class WorkoutSheetAdmin(admin.ModelAdmin):
    search_fields = ["user_signature",]
    list_display = ["student", "last_modified", "user_signature",]


@admin.register(WorkoutDay)
class WorkoutDayAdmin(admin.ModelAdmin):
    search_fields = ["week_day", "workout_sheet"]
    list_display = ["week_day",]


@admin.register(WorkoutExercice)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    search_fields = ["exercise_name",]
    list_display = ["exercise_name",]


@admin.register(WorkoutDayExercise)
class WorkoutDayExerciseAdmin(admin.ModelAdmin):
    search_fields = ["workout_day", "workout_exercise",]
    list_display = ["workout_exercise", "workout_day"]