from django.urls import path
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
]