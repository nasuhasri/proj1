from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Switches
from datetime import datetime, date, timedelta

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
    
    status1 = []
    switchTime1 = []
    for single_switch in switch1:
        status1.append(single_switch['status'])
        
        timestamp = int(single_switch['ts'])
        
        # Convert the Unix timestamp to a datetime object
        dt = datetime.fromtimestamp(timestamp)

        # Extract the time component from the datetime object
        time = dt.time()
        startTime = time.hour
        endTime = time.hour + 12
        
        if startTime <= time.hour < endTime:
            switchTime1.append(time)
            
    status2 = []
    switchTime2 = []
    for single_switch in switch2:
        status2.append(single_switch['status'])
        
        timestamp = int(single_switch['ts'])
        
        # Convert the Unix timestamp to a datetime object
        dt = datetime.fromtimestamp(timestamp)

        # Extract the time component from the datetime object
        time = dt.time()
        startTime = time.hour
        endTime = time.hour + 12
        
        if startTime <= time.hour < endTime:
            switchTime2.append(time)
    
    status3 = []
    switchTime3 = []
    for single_switch in switch3:
        status3.append(single_switch['status'])
        
        timestamp = int(single_switch['ts'])
        
        # Convert the Unix timestamp to a datetime object
        dt = datetime.fromtimestamp(timestamp)

        # Extract the time component from the datetime object
        time = dt.time()
        startTime = time.hour
        endTime = time.hour + 12
        
        if startTime <= time.hour < endTime:
            switchTime3.append(time)
            
    context = {
        "status1": status1,
        "switchTime1": switchTime1,
        "status2": status2,
        "switchTime2": switchTime2,
        "status3": status3,
        "switchTime3": switchTime3
    }
    
    return render(request, "graph.html", context)