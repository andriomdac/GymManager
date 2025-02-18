# Generated by Django 5.1.5 on 2025-02-11 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_workoutsheet_last_modified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutDayExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='trainings.workoutday')),
                ('workout_exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trainings.workoutexercice')),
            ],
        ),
    ]
