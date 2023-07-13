from django import forms
from .models import Etudiants

class Etudiantform(forms.ModelForm):

    class Meta:
        model =Etudiants
        fields =['nom','prenom','email','domaine_etudiant','code' ]
        labels ={'nom':'Nom',
                'prenom':'Prenom',
                'email':'Email',
                'domaine_etudiant':'Domaine Etude',
                'code':'Code'}
        widgets = {'nom':forms.TextInput(attrs={'class': 'form-control'}),
                'prenom':forms.TextInput(attrs={'class': 'form-control'}),
                'email':forms.EmailInput(attrs={'class': 'form-control'}),
                'domaine_etudiant':forms.TextInput(attrs={'class': 'form-control'}),
                'code':forms.TextInput(attrs={'class': 'form-control'})}

