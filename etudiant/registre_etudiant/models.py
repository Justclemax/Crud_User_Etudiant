from django.db import models

# Create your models here.
class Etudiants(models.Model):
    id_position =models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=34)
    domaine_etudiant = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return  f'Etudiant : {self.id_position} {self.nom}  {self.prenom}'