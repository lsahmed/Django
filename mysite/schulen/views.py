from django.shortcuts import render

def schulen(request):
    return render(request, "schulen/schulen.html")
