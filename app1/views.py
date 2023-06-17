from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Switches

def index(request):
    switches = Switches.objects.all()
    
    return render(request, "index.html", {
        "switches": switches
    })
    
def update_switch_status(request):
    print (request)
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
    
def alert_page(request):
    return render(request, "alert.html", {"test": "test"})