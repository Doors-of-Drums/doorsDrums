from pyexpat import model
from django.db import models

# Create your models here.
class Usuario(models.Model):
    # tabla de usuarios
    nombre_usuario = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    '''
    "id_usuario"	INTEGER,
	"Nombre_de_usuario"	TEXT NOT NULL, YA
	"Pais"	TEXT NOT NULL,
	"Fecha_de_nacimiento"	TEXT NOT NULL,
	"Contraseña"	TEXT NOT NULL,
	"Correo"	TEXT NOT NULL,
	"Apellido_materno"	TEXT NOT NULL,
	"Apellido_paterno"	TEXT NOT NULL,
	"Genero"	TEXT NOT NULL,
	"Telefono"	TEXT NOT NULL,
	"Foto"	TEXT NOT NULL,
	"Status"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id_usuario")
    '''
