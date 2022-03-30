from pyexpat import model
from django.db import models

# Create your models here.


class Usuario(models.Model):
    # tabla de usuarios
    nombre = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50)
    pais = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    contrasena = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    telefono = models.CharField(max_length=200)
    foto = models.CharField(max_length=100)
    status = models.BooleanField(default=False)


class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    genero_mus = models.CharField(max_length=100)
    ritmo = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=100)


class Historial_partida(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    puntos = models.PositiveIntegerField()  # desde 0 a 2147483647
    fecha = models.DateTimeField()
    tiempo_jugado = models.PositiveIntegerField()
