from django.urls import path
from . import views

urlpatterns = [
    path('', views.schulen, name='schulen'),
    path('<int:anime_id>/', views.anime_detail, name='anime_d'),
    path('stores/', views.stores_view, name="stores"),
]
