from django.shortcuts import render
from .models import AnimeVariety, Store
from django.shortcuts import get_object_or_404
from .forms import AnimeVarietyForm

def schulen(request):
    animes = AnimeVariety.objects.all() # <- this will return an array.
    return render(request, "schulen/schulen.html", {"animes": animes,})

def anime_detail(request, anime_id):
    anime_d = get_object_or_404(AnimeVariety, pk=anime_id)
    return render(request, "schulen/anime_details.html", {"anime_d":anime_d})

def stores_view(request):
    stores = None
    if request.method == "POST":
        form = AnimeVarietyForm(request.POST)
        if form.is_valid():
            anime_variety = form.cleaned_data["anime_variety"]
            stores = Store.objects.filter(anime_varities=anime_variety)
            print(f"Store found {stores}")
    else:
        form = AnimeVarietyForm()
    return render(request, "schulen/stores.html", {"form": form, "stores": stores})
