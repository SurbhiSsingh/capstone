from django import forms
from blog.models import  Post  # ✅ Try using 'blog.models'

class BlogForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ['title', 'content','author','slug','profile_photo']
