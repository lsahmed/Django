from django.shortcuts import render
from .models import AnimeVariety

def schulen(request):
    animes = AnimeVariety.objects.all() # <- this will return an array.
    return render(request, "schulen/schulen.html", {"animes": animes})

