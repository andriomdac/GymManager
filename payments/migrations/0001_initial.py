# Generated by Django 5.1.5 on 2025-02-01 21:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=30)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(default=datetime.datetime(2025, 2, 1, 21, 17, 45, 961401, tzinfo=datetime.timezone.utc))),
                ('next_paymentdate', models.DateField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, default=0, null=True)),
                ('observations', models.CharField(blank=True, max_length=100, null=True)),
                ('user_signature', models.CharField(blank=True, default='Sem assinatura', max_length=100, null=True)),
                ('student', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='pagamentos', to='students.student')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.paymentmethod')),
                ('payment_package', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='paypkg', to='payments.paymentpackage')),
            ],
        ),
    ]
