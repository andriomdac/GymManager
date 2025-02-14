from django import forms
from trainings.models import WorkoutDay

class WorkoutDayForm(forms.ModelForm):
    class Meta:
        model = WorkoutDay
        fields = ["week_day",]
        widgets = {
            "week_day": forms.Select(
                attrs={
                    "class": "form-control"
                }
                )
        }