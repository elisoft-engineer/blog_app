from .models import Blog
from django import forms

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
