# models.py
from django.db import models

class TodoTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner_email = models.EmailField() 

    def __str__(self):
        return self.title


class TaskSchedule(models.Model):
    task = models.OneToOneField(TodoTask, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=None, blank=True, null=True)
    
    def __str__(self):
        return f"{self.task.title} - {self.due_date}"



class TaskReschedule(models.Model):
    task_schedule = models.ForeignKey(TaskSchedule, on_delete=models.CASCADE)
    new_due_date = models.DateTimeField()
    rescheduled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_schedule.task.title} - Rescheduled to {self.new_due_date}"


class TaskReminder(models.Model):
    task = models.ForeignKey(TodoTask, on_delete=models.CASCADE)
    reminder_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.task.title} - Reminder at {self.reminder_datetime}"