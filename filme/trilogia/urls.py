from django.urls import path
from trilogia.views import home, sequencias, elenco

urlpatterns = [
    path('', home),
    path('sequencias/', sequencias),
    path('elenco/', elenco),
]