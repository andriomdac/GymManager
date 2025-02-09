from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name}'