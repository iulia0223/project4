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
from playlists import views


urlpatterns = [
    path('admin/', admin.site.urls),
]
# playlists/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_all_users, name='get_all_users'),
    path('users/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'),
    path('playlists/', views.get_all_playlists, name='get_all_playlists'),
    path('playlists/<int:playlist_id>/', views.get_playlist_by_id, name='get_playlist_by_id'),
    path('playlists/<int:playlist_id>/tracks/', views.get_tracks_of_playlist, name='get_tracks_of_playlist'),
    # Додайте інші URL-шляхи та пов'язані функції
]

# playlist_service/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('playlists.urls')),
]
