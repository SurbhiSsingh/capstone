from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'authors', 'year', 'topic', 'category', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'authors': forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'year': forms.NumberInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'topic': forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'category': forms.Select(attrs={'class': 'border rounded px-3 py-2 w-full'}),
            'link': forms.URLInput(attrs={'class': 'border rounded px-3 py-2 w-full'}),
        }