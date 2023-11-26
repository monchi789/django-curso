from django.db import models

# Imports the model
from applications.departamento.models import Departamento

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajos', choices=JOB_CHOICES, max_length=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField('Imagen', upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Mis empleados'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')


    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name