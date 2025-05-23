from django.shortcuts import render
from .models import MissionVision  # if you use a model

def mission_vision(request):
    mv = MissionVision.objects.first()  # or however you fetch the data
    return render(request, 'mission/mission_vision.html', {'mv': mv})

