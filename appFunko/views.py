from django.shortcuts import render
from .models import Funko

# Create your views here.

def index(request):
    context={}
    return render(request, 'appFunko/index.html',context)

def carrito(request):
    context={}
    return render(request, 'appFunko/carrito.html',context)

def login(request):
    return render(request, 'appFunko/login.html')

def map(request):
    return render(request,'appFunko/map.html')

def nosotros(request):
    return render(request,'appFunko/nosotros.html')

def registro(request):
    return render(request, 'appFunko/registro.html')

def harry(request):
    funkos = Funko.objects.all()
    data = {"productos":funkos}
    return render(request, 'appFunko/Sec.harry.html',data)

def disney(request):
    funkos = Funko.objects.all()
    data = {"productos":funkos}
    return render(request, 'appFunko/Sec.Disney.html',data)

def simpsons(request):
    funkos = Funko.objects.all()
    data = {"productos":funkos}
    return render(request, 'appFunko/Sec.simpsons.html',data)

def anime(request):
    funkos = Funko.objects.all()
    data = {"productos":funkos}
    return render(request, 'appFunko/Sec.anime.html',data)