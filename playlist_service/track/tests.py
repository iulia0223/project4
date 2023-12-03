from django.test import TestCase
from .models import Track
from django.urls import reverse

class TrackTests(TestCase):
    def setUp(self):
        self.track = Track.objects.create(name='Test Track', artist='Test Artist')

    def test_track_model(self):
        self.assertEqual(self.track.name, 'Test Track')
        self.assertEqual(self.track.artist, 'Test Artist')

    def test_track_list_view(self):
        response = self.client.get(reverse('track-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Track')

    def test_track_detail_view(self):
        response = self.client.get(reverse('track-detail', args=[str(self.track.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Track')
        self.assertContains(response, 'Test Artist')
