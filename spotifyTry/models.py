from pydoc import describe
from django.db import models

# Create your models here.


class TipoDocumento(models.Model):
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.descripcion)

    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=600)


class Ciudad(models.Model):
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.descripcion)

    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=600)


class Persona(models.Model):
    def __str__(self):
        return ("usuario:%s nombre: %s apellido: %s " %
                (self.usuario, self.nombres, self.apellidos))

    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento = models.FileField(upload_to="uploads/")
    lugarderecidencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechadenacimiento = models.DateField()
    email = models.EmailField()
    usuario = models.CharField(max_length=100, unique=True)
    telefono = models.IntegerField()
    password = models.CharField(max_length=100)
