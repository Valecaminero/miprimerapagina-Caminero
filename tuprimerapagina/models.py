from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_nacimiento= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion_semanas = models.IntegerField(default=4)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_nacimiento= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
 
class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'

