from django.test import TestCase
from .models import PlaylistTrack
from playlist.models import Playlist
from track.models import Track

class PlaylistTrackTests(TestCase):
    def setUp(self):
        self.playlist = Playlist.objects.create(name='Test Playlist')
        self.track = Track.objects.create(name='Test Track', artist='Test Artist')
        self.playlisttrack = PlaylistTrack.objects.create(playlist=self.playlist, track=self.track)

    def test_playlisttrack_model(self):
        self.assertEqual(self.playlisttrack.playlist, self.playlist)
        self.assertEqual(self.playlisttrack.track, self.track)

