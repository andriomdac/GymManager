from django.db import models
from students.models import Student


WEEK_DAYS = [
    ["SUNDAY", "DOMINGO"],
    ["MONDAY", "SEGUNDA"],
    ["TUESDAY", "TERÇA"],
    ["WEDNESDAY", "QUARTA"],
    ["THURSDAY", "QUINTA"],
    ["FRIDAY", "SEXTA"],
    ["SATURDAY", "SÁBADO"],

]


class WorkoutExercice(models.Model):
    exercise_name = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise_name


class WorkoutSheet(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.PROTECT,
        related_name='trainings'
        )
    last_modified = models.DateTimeField(auto_now=True)
    user_signature = models.CharField(
        blank=True,
        null=True,
        default='No user signature',
        max_length=100
        )
    observations = models.TextField(default='', max_length=200)
    def __str__(self):
        return f"Workout Sheet - {self.student}"


class WorkoutDay(models.Model):
    workout_sheet = models.ForeignKey(
        to=WorkoutSheet,
        on_delete=models.CASCADE,
        related_name='days'
        )
    week_day = models.CharField(
        choices=WEEK_DAYS, max_length=10
        )
    def __str__(self):
        day_dict = dict(WEEK_DAYS)
        return day_dict.get(self.week_day, self.week_day)

class WorkoutDayExercise(models.Model):
    workout_day = models.ForeignKey(
        to=WorkoutDay,
        on_delete=models.CASCADE,
        related_name='exercises'
        )
    workout_exercise = models.ForeignKey(
        to=WorkoutExercice,
        on_delete=models.PROTECT
        )
    observations = models.TextField(default='', max_length=200)

    def __str__(self):
        return f"{self.workout_day} - {self.workout_exercise}"