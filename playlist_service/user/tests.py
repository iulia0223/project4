from django.test import TestCase
from .models import User
from django.urls import reverse

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com')

    def test_user_model(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_list_view(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_user_detail_view(self):
        response = self.client.get(reverse('user-detail', args=[str(self.user.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'testuser@example.com')
