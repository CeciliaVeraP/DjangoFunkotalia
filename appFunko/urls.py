from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('carrito',views.carrito, name='carrito'),
    path('login', views.login, name='login'),
    path('map',views.map, name='map'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('registro', views.registro, name='registro'),
    path('Harry Potter', views.harry , name='Sec.harry'),
    path('Sec.Disney', views.disney , name='Sec.Disney'),
    path('Sec.simpsons', views.simpsons , name='Sec.simpsons'),
    path('Sec.anime', views.anime , name='Sec.anime'),
    path('agregar-producto', views.agregar_producto , name='agregar-producto'),
    path('listar-producto', views.listar_funko , name='listar-producto'),
    path('modificar-producto/<id>', views.modificar_funko , name='modificar-producto'),
    path('eliminat-producto/<id>', views.eliminar_funko , name='eliminar-producto'),
    path('accounts/',include('django.contrib.auth.urls')),
]