"""
URL configuration for playlist_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# playlist_service/urls.py
from django.urls import path
from .views import get_playlist, create_playlist

urlpatterns = [
    path('api/playlists/<int:playlist_id>/', get_playlist, name='get_playlist'),
    path('api/playlists/create/', create_playlist, name='create_playlist'),
    # Додайте інші URL-шляхи для інших функціональностей вашого проекту
]

# playlist_service/urls.py
from django.urls import path
from .views import get_playlist_track, add_track_to_playlist

urlpatterns = [
    path('api/playlist-tracks/<int:playlist_id>/', get_playlist_track, name='get_playlist_track'),
    path('api/playlist-tracks/add-track/', add_track_to_playlist, name='add_track_to_playlist'),
    # Додайте інші URL-шляхи для інших функціональностей вашого проекту
]


# playlist_service/urls.py
from django.urls import path
from .views import get_track, create_track

urlpatterns = [
    path('api/tracks/<int:track_id>/', get_track, name='get_track'),
    path('api/tracks/create/', create_track, name='create_track'),
    # Додайте інші URL-шляхи для інших функціональностей вашого проекту
]


# playlist_service/urls.py
from django.urls import path
from .views import get_user, create_user

urlpatterns = [
    path('api/users/<int:user_id>/', get_user, name='get_user'),
    path('api/users/create/', create_user, name='create_user'),
    # Додайте інші URL-шляхи для інших функціональностей вашого проекту
]
