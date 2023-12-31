# Generated by Django 4.2.7 on 2023-11-14 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateTimeField()),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todoapp.todotask')),
            ],
        ),
        migrations.CreateModel(
            name='TaskReschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_due_date', models.DateTimeField()),
                ('rescheduled_at', models.DateTimeField(auto_now_add=True)),
                ('task_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.taskschedule')),
            ],
        ),
    ]
