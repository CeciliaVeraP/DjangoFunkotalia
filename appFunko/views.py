from django.shortcuts import render, redirect, get_object_or_404
from .models import Funko
from .forms import FunkoForm

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

def agregar_producto(request):
    data = { 'form': FunkoForm()}

    if request.method == 'POST':
        formulario = FunkoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Guardado exitosamente"
        else:
            data['form'] = formulario
    return render(request, 'appFunko/producto/agregar.html',data)

def listar_funko(request):
    funkos = Funko.objects.all()
    data = {"productos":funkos}
    return render(request, 'appFunko/producto/listar.html', data)

def modificar_funko(request, id):
    funkos = get_object_or_404(Funko, id=id)
    data = { 'form': FunkoForm(instance=funkos)}
    if request.method == 'POST':
        formulario = FunkoForm(data=request.POST, instance=funkos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto modificado exitosamente"
            return redirect(to="listar-producto")
        data['form'] = formulario

    return render(request, 'appFunko/producto/modificar.html', data)

def eliminar_funko(request, id):
    funkos = get_object_or_404(Funko, id=id)
    funkos.delete()
    return redirect(to="listar-producto")
