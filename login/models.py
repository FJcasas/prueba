from django.db import models
from django.forms import CharField

# Create your models here.
class registrar(models.Model):
    nombre = CharField(max_length=100)
    password = CharField(max_length=100)
