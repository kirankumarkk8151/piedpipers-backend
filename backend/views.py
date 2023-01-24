from django.shortcuts import render
import base64
from django.http import JsonResponse
from .models import Team,EventHappened,UpcommingEvents
from django.views.decorators.cache import never_cache

@never_cache
def get_teams(request):
    teams = Team.objects.all()
    teams_data = []
    for team in teams:
       
        teams_data.append({
            
            'name': team.name,
            'information': team.information,
            'image':team.image.url,
            'role':team.role,
           
        })
    return JsonResponse(teams_data, safe=False)
@never_cache
def get_eventshappened(request):
    events = EventHappened.objects.all()
    events_data = []
    for event in events:
       
        events_data.append({
            
            'title': event.title,
            'information': event.information,
            'image':event.image.url,
           
        })
    return JsonResponse(events_data, safe=False)
@never_cache
def get_upcommingevents(request):
    events = UpcommingEvents.objects.all()
    events_data = []
    for event in events:
       
        events_data.append({
            
            'name': event.title,
            'information': event.desc,
            'register':event.registration,
           
        })
    return JsonResponse(events_data, safe=False)



