from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Estudiante(Persona):
    materias = models.IntegerField()


class Profesor(Persona):
    profesion = models.CharField(max_length=20)


class Curso(models.Model):
    name = models.CharField(max_length=50)
    idc = models.IntegerField()
    def __str__(self):
        return f"Curso: {self.name}, Camada: {self.idc}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    entregado = models.BooleanField
