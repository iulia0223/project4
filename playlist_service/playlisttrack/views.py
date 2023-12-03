from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import PlaylistTrack

class PlaylistTrackListView(ListView):
    model = PlaylistTrack
    template_name = 'playlisttrack/playlisttrack_list.html'
    context_object_name = 'playlisttracks'

class PlaylistTrackDetailView(DetailView):
    model = PlaylistTrack
    template_name = 'playlisttrack/playlisttrack_detail.html'
    context_object_name = 'playlisttrack'
