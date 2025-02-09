from django.contrib import admin
from payments.models import (
    Payment,
    PaymentMethod,
    PaymentPackage,
    PaymentValue,
)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ["user_signature",]
    list_display = [
        "student",
        "payment_date",
        "next_payment_date",
        "payment_package",
        "observations",
        ]

@admin.register(PaymentValue)
class PaymentValueAdmin(admin.ModelAdmin):
    search_fields = ["value",]
    list_display = ["payment", "value",]

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    search_fields = ["method",]
    list_display = ["method",]

@admin.register(PaymentPackage)
class PaymentPackage(admin.ModelAdmin):
    search_fields = ["package",]
    list_display = ["package",]