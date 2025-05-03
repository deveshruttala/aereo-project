# tasks/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task
# No need for logging imports unless you are actively debugging complex issues

class TaskAPITestCase(APITestCase):
    def setUp(self):
        """Create initial tasks for testing."""
        self.task_data_1 = {
            'title': 'Test Task 1',
            'description': 'This is a test task.',
            'completed': False,
            'date': '2025-05-03'
        }
        self.task_data_2 = {
            'title': 'Test Task 2',
            'description': 'This is another test task.',
            'completed': True,
            'date': '2025-05-04'
        }

        # Create two tasks
        self.task_1 = Task.objects.create(**self.task_data_1)
        self.task_2 = Task.objects.create(**self.task_data_2)

        # URL for the task list
        self.list_url = reverse('task-list')

    def test_list_tasks(self):
        """Test retrieving all tasks."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # *** FIX: Check length of the 'results' list ***
        self.assertEqual(len(response.data['results']), 2, f"Expected 2 tasks, found {len(response.data.get('results', []))}. Response: {response.data}")

    def test_create_task(self):
        """Test creating a new task."""
        initial_count = Task.objects.count()
        data = {
            'title': 'New Task',
            'description': 'A new task created by test.',
            'completed': False,
            'date': '2025-05-05'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Detail view response is typically not paginated
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(Task.objects.count(), initial_count + 1)

    def test_update_task(self):
        """Test updating an existing task partially using PATCH."""
        update_data = {'completed': True}
        task_url = reverse('task-detail', kwargs={'pk': self.task_1.pk})
        response = self.client.patch(task_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Detail view response is typically not paginated
        self.assertEqual(response.data['completed'], True)
        self.task_1.refresh_from_db()
        self.assertTrue(self.task_1.completed)

    def test_delete_task(self):
        """Test deleting a task."""
        initial_count = Task.objects.count()
        task_url = reverse('task-detail', kwargs={'pk': self.task_1.pk})
        delete_response = self.client.delete(task_url) # Use different name
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure the task is deleted from DB
        self.assertEqual(Task.objects.count(), initial_count - 1)
        with self.assertRaises(Task.DoesNotExist):
             Task.objects.get(pk=self.task_1.pk)

        # Verify list endpoint count after deletion
        list_response = self.client.get(self.list_url) # Use different name
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        # *** FIX: Check length of the 'results' list ***
        self.assertEqual(len(list_response.data['results']), 1, f"Expected 1 task after delete, found {len(list_response.data.get('results', []))}. Response: {list_response.data}")

    def test_filter_tasks_by_completed(self):
        """Test filtering tasks by 'completed' field."""
        response = self.client.get(self.list_url, {'completed': 'True'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # *** FIX: Check length of the 'results' list ***
        self.assertEqual(len(response.data['results']), 1, f"Expected 1 completed task, found {len(response.data.get('results', []))}. Response: {response.data}")
        # Optional: Stronger assertion
        self.assertEqual(response.data['results'][0]['title'], self.task_2.title)

    def test_filter_tasks_by_date(self):
        """Test filtering tasks by 'date' field."""
        response = self.client.get(self.list_url, {'date': '2025-05-04'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # *** FIX: Check length of the 'results' list ***
        self.assertEqual(len(response.data['results']), 1, f"Expected 1 task for date 2025-05-04, found {len(response.data.get('results', []))}. Response: {response.data}")
        # Optional: Stronger assertion
        self.assertEqual(response.data['results'][0]['title'], self.task_2.title)