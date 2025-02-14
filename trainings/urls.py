from django.urls import path
from trainings.views import training_day_add_view, training_sheet_view

urlpatterns = [
    path('', training_sheet_view, name='training_sheet_list'),
    path('day_add/', training_day_add_view, name='training_day_add'),
]