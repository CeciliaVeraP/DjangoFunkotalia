from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=60)
    def __str__(self):
        return self.nombreCategoria

class estado (models.Model):
    estadoFunko= models.CharField(max_length=10)
    def __str__(self):
        return self.estadoFunko


class Funko(models.Model):
    nombre = models.CharField(max_length=70)
    detalle = models.CharField(max_length=70, null=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estadoFunko= models.ForeignKey(estado, on_delete =models.PROTECT, null=True)

    def __str__(self):
        return self.nombre
    
    