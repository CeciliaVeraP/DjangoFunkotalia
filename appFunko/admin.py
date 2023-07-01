from django.contrib import admin
from .models import Categoria,Funko, estado
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Funko)
admin.site.register(estado)