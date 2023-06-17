from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Switches

def index(request):
    switches = Switches.objects.all()
    
    return render(request, "index.html", {
        "switches": switches
    })