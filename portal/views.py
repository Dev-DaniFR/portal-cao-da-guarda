from django.shortcuts import render
from .models import Campaign, Event


def home(request):
    campaigns = Campaign.objects.filter(is_active=True)
    events = Event.objects.filter(is_active=True).order_by('date')

    context = {
        'campaigns': campaigns,
        'events': events,
    }

    return render(request, 'portal/home.html', context)

def sobre(request):
    return render(request, 'portal/sobre.html')

def como_ajudar(request):
    return render(request, 'portal/como_ajudar.html')

def contato(request):
    return render(request, 'portal/contato.html')

def adocao(request):
    return render(request, 'portal/adocao.html')