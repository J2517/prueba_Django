from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.auth_headers = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        self.task = Task.objects.create(title='Tarea inicial', user=self.user)

    def test_list_tasks(self):
        url = '/tasks/'
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = '/tasks/'
        data = {'title': 'Nueva tarea'}
        response = self.client.post(url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_detail(self):
        url = f'/tasks/{self.task.id}/'
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        url = f'/tasks/{self.task.id}/'
        data = {'title': 'Actualizada', 'completed': True}
        response = self.client.put(url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Actualizada')
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        url = f'/tasks/{self.task.id}/'
        response = self.client.delete(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_unauthenticated_access(self):
        url = '/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
