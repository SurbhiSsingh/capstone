from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'degree', 'year', 'current_affiliation', 'profile_photo', 'bio']