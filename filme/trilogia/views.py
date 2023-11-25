from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def sequencias(request):
    return render(request,"sequencias.html")

def elenco(request):
    return render(request, "elenco.html")