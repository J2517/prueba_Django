from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_create_task(self):
        task = Task.objects.create(
            title='Tarea de prueba',
            description='Descripción de prueba',
            user=self.user
        )
        self.assertEqual(task.title, 'Tarea de prueba')
        self.assertFalse(task.completed)
        self.assertEqual(task.user, self.user)

    def test_str_representation(self):
        task = Task.objects.create(title='Mi tarea', user=self.user)
        self.assertEqual(str(task), 'Mi tarea') 
