from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Track

class TrackListView(ListView):
    model = Track
    template_name = 'track/track_list.html'
    context_object_name = 'tracks'

class TrackDetailView(DetailView):
    model = Track
    template_name = 'track/track_detail.html'
    context_object_name = 'track'
