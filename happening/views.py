from django.shortcuts import render, get_object_or_404
from .models import Event

def events_list(request):
    events = Event.objects.all()
    return render(request, 'happening.html', {'events': events})

def events_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'happening_detail.html', {'event': event})
