from django.shortcuts import render,get_object_or_404
from .models import Event

# Create your views here.

def index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'current/index.html', context)


def details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    return render(request,'current/details.html',{'event':event})


def update_event(request, event_id):
    events = get_object_or_404(Event, pk=event_id)
    return render(request, 'current/index.html',{'events':events})