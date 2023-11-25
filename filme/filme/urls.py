from django.contrib import admin
from django.urls import path, include 
from filme.views import home, sequencias, elenco

urlpatterns = [
    path('', include('trilogia.urls')),
    path('home/', home),
    path('sequencias/', sequencias),
    path('elenco/', elenco),
]