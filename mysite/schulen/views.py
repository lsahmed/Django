from django.shortcuts import render
from .models import AnimeVariety
from django.shortcuts import get_object_or_404

def schulen(request):
    animes = AnimeVariety.objects.all() # <- this will return an array.
    return render(request, "schulen/schulen.html", {"animes": animes})

def anime_detail(request, anime_id):
    anime_d = get_object_or_404(AnimeVariety, pk=anime_id)
    return render(request, "schulen/anime_details.html", {"anime_d":anime_d})
