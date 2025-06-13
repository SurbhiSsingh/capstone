from django import forms
from .models import MissionVision

class MissionVisionForm(forms.ModelForm):
    class Meta:
        model = MissionVision
        fields = ['mission_text', 'vision_text']