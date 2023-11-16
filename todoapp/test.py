
from django.test import TestCase

from .models import TodoTask
from .models import TaskSchedule
import datetime

class TodoTaskModelTestCase(TestCase):

    def test_create_todo_task(self):
        # Create a TodoTask object
        task = TodoTask.objects.create(
            title='Test Task',
            description='This is a test task.',
            owner_email='anushri@example.com'
        )

       
        retrieved_task = TodoTask.objects.get(title='Test Task')

        # Perform assertions to check if the data matches the expected values
        self.assertEqual(retrieved_task.title, 'Test Task')
        self.assertEqual(retrieved_task.description, 'This is a test task.')
        self.assertEqual(retrieved_task.owner_email, 'anushri@example.com')

class TaskScheduleTestCase(TestCase):
    def setUp(self):
       
        todo_task = TodoTask.objects.create(title="Sample Task", description="Sample description")

    
        self.task_schedule = TaskSchedule.objects.create(task=todo_task, due_date=datetime.datetime.now())

    def test_task_schedule_str_method(self):

        expected_str = f"{self.task_schedule.task.title} - {self.task_schedule.due_date}"
        self.assertEqual(str(self.task_schedule), expected_str)

    def test_task_schedule_attributes(self):
       
        self.assertEqual(self.task_schedule.task.title, "Sample Task")
        self.assertIsNotNone(self.task_schedule.due_date)

    def test_task_schedule_creation(self):
       
        todo_task = TodoTask.objects.create(title="Another Task", description="Another description")
        task_schedule = TaskSchedule.objects.create(task=todo_task, due_date=datetime.datetime.now())
        self.assertEqual(TaskSchedule.objects.count(), 2)

    def test_task_schedule_deletion(self):
        
        task_schedule_id = self.task_schedule.id
        self.task_schedule.delete()
        self.assertIsNone(TaskSchedule.objects.filter(id=task_schedule_id).first())