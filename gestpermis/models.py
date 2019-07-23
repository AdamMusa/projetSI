from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProfilCandidat(models.Model):
    #image = models.ImageField(required=False)
    pass


class Candidat(models.Model):
    #profil = models.OneToOneField(ProfilCandidat,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    data_burth = models.DateTimeField()
    lieu_burth = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username

class CapitalPoint(models.Model):
    candidat = models.OneToOneField(Candidat,on_delete = models.CASCADE)
    point = models.IntegerField(default=50)
    add_at = models.DateTimeField(auto_now=True)

class PermisConducteur(models.Model):
    candidat = models.OneToOneField(Candidat,on_delete = models.CASCADE)
    capital = models.OneToOneField(CapitalPoint,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)




class Categorie(models.Model):
    permis = models.ForeignKey(PermisConducteur,on_delete=models.CASCADE)
    grade = models.IntegerField()
    add_at = models.DateTimeField(auto_now=True)



class Agent(models.Model):
    candidat = models.ManyToManyField(User)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)


class Infraction(models.Model):
    pass