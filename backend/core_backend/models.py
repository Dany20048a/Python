from django.db import models

# Create your models here.
#el id ya esta declarado, 3 tablas
#Base de datos_tablas de base de datos ORM=OBJECT RELATIONAL MAMPING, MVC, se maneja con clases
class Sala(models.Model): 
    nombre = models.CharField(max_length=255, blank=True, null=False)
    tamaño = models.IntegerField(null=True, blank=True)  # Metros cuadrados
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    aforo = models.IntegerField(null=True, blank=True)

#usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    identificador = models.IntegerField(blank=True, null=True)  # Utiliza IntegerField #identificador a parte del ID de manera aleatoria 

class Reservacion(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_final = models.TimeField(null=True, blank=True)
    personas = models.IntegerField(null=True, blank=True)
