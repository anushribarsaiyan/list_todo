# serializers.py
from rest_framework import serializers
from .models import TodoTask, TaskSchedule, TaskReschedule, TaskReminder

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = '__all__'


class TaskScheduleSerializer(serializers.ModelSerializer):
    task = TodoTaskSerializer(read_only=True)

    class Meta:
        model = TaskSchedule
        fields = '__all__'


class TaskRescheduleSerializer(serializers.ModelSerializer):
    task_schedule = TaskScheduleSerializer()

    class Meta:
        model = TaskReschedule
        fields = '__all__'


class TaskReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskReminder
        fields = '__all__'