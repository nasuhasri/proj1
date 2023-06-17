from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Switches

def index(request):
    switches = Switches.objects.all()
    
    return render(request, "index.html", {
        "switches": switches
    })
    
def update_switch_status(request):
    if request.method == 'POST':
        switch_id = request.POST.get('switch_id')
        status = request.POST.get('status')

        try:
            switch_obj = Switches.objects.get(id=switch_id)
            switch_obj.status = status
            switch_obj.save()
            return JsonResponse({'success': True})
        except Switches.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Switch not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})

def auto_update_status(request):
    switches = Switches.objects.all()
    
    for switch in switches:
        if switch.t1 == switch.t2 == switch.t3 == switch.t4 == switch.t5 == 0:
            status = 0
        else:
            status = 1
        
        switch_obj = Switches.objects.get(id=switch.id)
        switch_obj.status = status
        switch_obj.save()
     
def alert_page(request):
    switches = Switches.objects.all()
    
    return render(request, "alert.html", {
        "switches": switches,
    })
    
def display_graph(request):
    switch1 = Switches.objects.filter(sw="S1").values()
    switch2 = Switches.objects.filter(sw="S2").values()
    switch3 = Switches.objects.filter(sw="S3").values()
    
    return render(request, "graph.html", {
        "switch1": switch1,
        "switch2": switch2,
        "switch3": switch3,
    })