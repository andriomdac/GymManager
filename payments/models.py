from django.db import models
from students.models import Student
from django.utils import timezone


class PaymentPackage(models.Model):    
    package = models.CharField(max_length=30)

    def __str__(self):
        return self.package


class PaymentMethod(models.Model):
    method = models.CharField(max_length=20)

    def __str__(self):
        return self.method


class Payment(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.PROTECT,
        related_name='payments',
        default=0
        )
    payment_date = models.DateField(
        default=timezone.localdate()
        )
    next_payment_date = models.DateField(
        blank=True,
        null=True,
        )
    payment_package = models.ForeignKey(
        default=0,
        to=PaymentPackage,
        on_delete=models.PROTECT
        )
    observations = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )
    user_signature = models.CharField(
        blank=True,
        null=True,
        default='No user signature',
        max_length=100
        )
    active = models.BooleanField(
        default=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return f'Payment for {self.student}: {self.payment_date}'


class PaymentValue(models.Model):
    payment = models.ForeignKey(
        to=Payment,
        on_delete=models.CASCADE,
        related_name='values'
        )
    method = models.ForeignKey(
        to=PaymentMethod,
        on_delete=models.PROTECT,
        related_name='payment_methods',
        default=1
        )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    
    def __str__(self):
        return f"{self.value}"