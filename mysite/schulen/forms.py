from django import forms 
from .models import AnimeVariety

class AnimeVarietyForm(forms.Form):
    anime_variety = forms.ModelChoiceField(queryset=AnimeVariety.objects.all(), label="Select anime variety")
    