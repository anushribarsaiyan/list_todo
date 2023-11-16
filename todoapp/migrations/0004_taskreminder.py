# Generated by Django 4.2.7 on 2023-11-14 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_taskschedule_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_datetime', models.DateTimeField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.todotask')),
            ],
        ),
    ]
