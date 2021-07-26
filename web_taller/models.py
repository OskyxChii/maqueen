from typing import Pattern
from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

# imagenes index

class Sliderindex(models.Model):
    ident = models.CharField(max_length=15, primary_key=True)
    imagen = models.ImageField(upload_to='index', null=True)

    def __str__(self) -> str:
        return self.ident

# categorias

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Automobil(models.Model):
    patente = models.CharField(primary_key=True,max_length=7)
    modelo = models.TextField(max_length=25)
    año = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='index',null=True)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente