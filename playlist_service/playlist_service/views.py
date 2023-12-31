# playlist_service/views.py
from django.http import HttpResponse

def get_playlist(request, playlist_id):
    # Логіка для отримання плейлисту
    return HttpResponse(f'Getting playlist {playlist_id}')

def create_playlist(request):
    # Логіка для створення плейлисту
    return HttpResponse('Creating playlist')

def get_playlist_track(request, playlist_id):
    # Логіка для отримання треку плейлисту
    return HttpResponse(f'Getting tracks for playlist {playlist_id}')

def add_track_to_playlist(request):
    # Логіка для додавання треку до плейлисту
    return HttpResponse('Adding track to playlist')

def get_track(request, track_id):
    # Логіка для отримання інформації про трек
    return HttpResponse(f'Getting track {track_id}')

def create_track(request):
    # Логіка для створення треку
    return HttpResponse('Creating track')

def get_user(request, user_id):
    # Логіка для отримання інформації про користувача
    return HttpResponse(f'Getting user {user_id}')

def create_user(request):
    # Логіка для створення користувача
    return HttpResponse('Creating user')

# playlist_service/views.py
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Welcome to the homepage!')

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

def get_playlist(request, playlist_id):
    try:
        # Логіка для отримання плейлисту
        # ...

        # Якщо плейлист не знайдено, повертаємо 404 (Not Found)
        if playlist_not_found_condition:
            return HttpResponseNotFound('Playlist not found')

        # Якщо все в порядку, повертаємо успішну відповідь
        return HttpResponse(f'Getting playlist {playlist_id}')
    except Exception as e:
        # Якщо виникає інша помилка, повертаємо 400 (Bad Request)
        return HttpResponseBadRequest(f'Bad Request: {str(e)}')
