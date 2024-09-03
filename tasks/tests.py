from django.test import TestCase
from .models import Task, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser', password='password')
        self.category = Category.objects.create(name='Work', color='blue')
        self.task = Task.objects.create(title='Test Task', owner=self.user, category=self.category)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
