# Generated by Django 5.1.5 on 2025-02-02 13:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payment_payment_date_alter_payment_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentpackage',
            name='value',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=datetime.datetime(2025, 2, 2, 13, 5, 46, 739375, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_package',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='payments.paymentpackage'),
        ),
        migrations.CreateModel(
            name='PaymentValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='values', to='payments.payment')),
            ],
        ),
    ]
