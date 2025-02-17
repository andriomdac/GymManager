from django.urls import path
from trainings.views import (
    create_new_training_sheet,
    training_sheet_list_view,
    training_sheet_detail_view,
    training_sheet_delete_view,
    training_sheet_day_add_view,
    training_sheet_day_delete_view,
    )


urlpatterns = [
    path('', training_sheet_list_view, name='training_sheet_list'),
    path('create_new/', create_new_training_sheet, name='create_new_training_sheet'),
    path('<int:sheet_id>/', training_sheet_detail_view, name='training_sheet_detail'),
    path('delete/<int:sheet_id>/', training_sheet_delete_view, name='training_sheet_delete'),
    path('<int:sheet_id>/day_add/', training_sheet_day_add_view, name='training_sheet_day_add'),
    path('<int:sheet_day>/delete/', training_sheet_day_delete_view, name='training_sheet_day_delete'),
]