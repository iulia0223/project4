from django.test import TestCase
from .models import Playlist
from django.urls import reverse

class PlaylistTests(TestCase):
    def setUp(self):
        self.playlist = Playlist.objects.create(name='Test Playlist')

    def test_playlist_model(self):
        self.assertEqual(self.playlist.name, 'Test Playlist')

    def test_playlist_list_view(self):
        response = self.client.get(reverse('playlist-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Playlist')

    def test_playlist_detail_view(self):
        response = self.client.get(reverse('playlist-detail', args=[str(self.playlist.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Playlist')

    def test_invalid_playlist_creation(self):
        # Викликаємо API для створення плейлисту із некоректними даними
        response = self.client.post(reverse('playlist-list'), data={'invalid_field': 'Invalid Value'})

        # Перевіряємо, чи повертається статус код 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
