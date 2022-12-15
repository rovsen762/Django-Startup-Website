from django.shortcuts import render
from .models import Team,SocMedia
from django.views.generic import ListView


# Create your views here.
def team(request):
    team = Team.objects.all()
    socmed = SocMedia.objects.all()
    context = {
        'team': team,
        'socmed': socmed,
    }
    return render(request, 'team.html', context)




    

    