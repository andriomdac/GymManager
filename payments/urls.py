from django.urls import path
from .views import add_payment, add_value, delete_value, delete_payment, unfinished_payment


urlpatterns = [
    path('add_payment/', add_payment, name='add_payment'),
    path('add_value/', add_value, name='add_value'),
    path('delete_value/', delete_value, name='delete_value'),
    path('delete_payment/', delete_payment, name='delete_payment'),
    path('unfinished_payment', unfinished_payment, name='unfinished_payment')
]