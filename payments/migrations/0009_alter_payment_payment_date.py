# Generated by Django 5.1.5 on 2025-02-06 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_payment_created_at_alter_payment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=datetime.datetime(2025, 2, 6, 0, 58, 47, 237910, tzinfo=datetime.timezone.utc)),
        ),
    ]
