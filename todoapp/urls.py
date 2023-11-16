# urls.py
from django.urls import path
from .views import TodoTaskListCreateView, TaskScheduleView, TaskRescheduleView



urlpatterns = [
    path('tasks/', TodoTaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:task_id>/schedule/', TaskScheduleView.as_view(), name='task_schedule'),
    path('tasks/<int:task_id>/reschedule/', TaskRescheduleView.as_view(), name='task-reschedule'),


]




