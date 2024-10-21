from django.urls import path
from . import views

urlpatterns = [
    path('', views.schulen, name='schulen'),
]
