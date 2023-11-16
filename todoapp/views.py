# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoTask, TaskSchedule, TaskReschedule
from .serializers import TodoTaskSerializer, TaskScheduleSerializer, TaskRescheduleSerializer
from rest_framework.response import Response


class TodoTaskListCreateView(APIView):
    def get(self, request):
        tasks = TodoTask.objects.all()
        serializer = TodoTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoTaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            TaskSchedule.objects.create(task=task, due_date=None)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TodoTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_object(self, pk):
        try:
            return TodoTask.objects.get(pk=pk)
        except TodoTask.DoesNotExist:
            pass


class TaskScheduleView(APIView):
    def get_object(self, task_id):
        try:
            return TaskSchedule.objects.get(task__id=task_id)
        except TaskSchedule.DoesNotExist:
            return None

    def get(self, request, task_id):
        schedule = self.get_object(task_id)
        if schedule is not None:
            serializer = TaskScheduleSerializer(schedule)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, task_id):
        schedule = self.get_object(task_id)
        if schedule is not None:
            serializer = TaskScheduleSerializer(schedule, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


class TaskRescheduleView(APIView):
    def post(self, request, task_id):
        schedule = TaskSchedule.objects.get(task_id=task_id)
        new_due_date = request.data.get('new_due_date')
        reschedule = TaskReschedule.objects.create(task_schedule=schedule, new_due_date=new_due_date)
        serializer = TaskRescheduleSerializer(reschedule)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

