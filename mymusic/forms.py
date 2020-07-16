from django import forms
from .models import Album

class albumsForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist_name',
            'released',  
            'img_url',
        ]
