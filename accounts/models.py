from django.db import models

# Create your models here.

class GenrePer(models.Model):
    nom = models.CharField(max_length=30)
    code = models.CharField(max_length=30)