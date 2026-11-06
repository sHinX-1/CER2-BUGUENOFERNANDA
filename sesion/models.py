from django.db import models

# Create your models here.
class Especie (models.Model):
    nombre = models.CharField(max_length=50, primary_key= True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    genero = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return str(self.genero)


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    sexo = models.ForeignKey(Genero, to_field='genero', on_delete=models.PROTECT)
    edad_aproximada = models.CharField(max_length=50, help_text="Ejemplo: 2 años y 3 meses")
    imagen = models.URLField(max_length=500)
    especie = models.ForeignKey(Especie, to_field='nombre', on_delete=models.PROTECT)

    def __str__(self):
            return str(self.nombre)