# playlist_service/urls.py
from django.contrib import admin
from django.urls import path
from .views import home_view, get_playlist, create_playlist, get_playlist_track, add_track_to_playlist, get_track, create_track, get_user, create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('api/playlists/<int:playlist_id>/', get_playlist, name='get_playlist'),
    path('api/playlists/create/', create_playlist, name='create_playlist'),
    path('api/playlist-tracks/<int:playlist_id>/', get_playlist_track, name='get_playlist_track'),
    path('api/playlist-tracks/add-track/', add_track_to_playlist, name='add_track_to_playlist'),
    path('api/tracks/<int:track_id>/', get_track, name='get_track'),
    path('api/tracks/create/', create_track, name='create_track'),
    path('api/users/<int:user_id>/', get_user, name='get_user'),
    path('api/users/create/', create_user, name='create_user'),
    # Додайте інші URL-шляхи для інших функціональностей вашого проекту
]
