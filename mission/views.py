from django.shortcuts import render, redirect
from .models import MissionVision
from .forms import MissionVisionForm

def mission_vision(request):
    mv = MissionVision.objects.all()  # Fetch all Mission & Vision entries
    return render(request, 'mission/mission_vision.html', {'mv': mv})

def add_mission_vision(request):
    if request.method == 'POST':
        form = MissionVisionForm(request.POST)
        if form.is_valid():
            form.save()  # Always create a new MissionVision object
            return redirect('mission_vision')  # Redirect to the Mission & Vision page
    else:
        form = MissionVisionForm()
    return render(request, 'mission/add_mission_vision.html', {'form': form})