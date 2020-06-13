from django.db import models


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombreAlumno = models.CharField(max_length=75)
    apellidoAlumno = models.CharField(max_length=75)
    direccionAlumno = models.CharField(max_length=75)
    telefonoAlumno = models.CharField(max_length=20)
    correoAlumno = models.EmailField(max_length=100)
    encargadoAlumno = models.CharField(max_length=75)
    telefonoEncargado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreAlumno, self.apellidoAlumno


class Grado(models.Model):
    id = models.AutoField(primary_key=True),
    Grado = models.CharField(max_length=25)
    def __str__(self):
        return self.Grado


class Seccion(models.Model):
    id = models.AutoField(primary_key=True),
    seccion = models.CharField(max_length=5)
    def __str__(self):
        return self.seccion
