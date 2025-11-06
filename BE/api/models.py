from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    genero = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    num_telefono = models.CharField(max_length=15)
    
    