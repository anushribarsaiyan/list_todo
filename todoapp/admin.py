from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TodoTask)
admin.site.register(TaskSchedule)
admin.site.register(TaskReschedule)
admin.site.register(TaskReminder)