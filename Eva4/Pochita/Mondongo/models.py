from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    nro_celular = models.CharField(max_length=9)
    direccion = models.TextField()
    ramos_a_cursar = models.ManyToManyField('Ramo', related_name='estudiante')

class Docente(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    nro_celular = models.CharField(max_length=9)
    direccion = models.TextField()
    ramos_a_impartir = models.ManyToManyField('Ramo', related_name='docente')

class Ramo(models.Model):
    nombre = models.CharField(max_length=60)
    cantidad_notas = models.PositiveSmallIntegerField()
    estado = models.BooleanField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    numero_horas = models.PositiveIntegerField()

    def estado_texto(self):
        return "activo" if self.estado else "inactivo"

    def __str__(self) -> str:
        return self.nombre