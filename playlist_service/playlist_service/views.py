from django.shortcuts import render

# Create your views here.
# playlists/views.py
from django.shortcuts import HttpResponse
from .models import User, Playlist, Track

def get_all_users(request):
    # Логіка для отримання всіх користувачів
    return HttpResponse("Get all users")

def get_user_by_id(request, user_id):
    # Логіка для отримання користувача за ID
    return HttpResponse(f"Get user by ID: {user_id}")

def get_all_playlists(request):
    # Логіка для отримання всіх плейлистів
    return HttpResponse("Get all playlists")

def get_playlist_by_id(request, playlist_id):
    # Логіка для отримання плейлиста за ID
    return HttpResponse(f"Get playlist by ID: {playlist_id}")

def get_tracks_of_playlist(request, playlist_id):
    # Логіка для отримання треків плейлиста за ID
    return HttpResponse(f"Get tracks of playlist by ID: {playlist_id}")
