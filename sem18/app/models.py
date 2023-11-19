from django.db import models

# Modelo de tabla medico
class medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return "String"

# Modelo de tabla paciente
class paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    sexo = models.CharField(max_length=1)
    altura = models.FloatField()
    medicoid = models.ForeignKey(medico, on_delete=models.CASCADE)

    def __str__(self):
        return "String"
