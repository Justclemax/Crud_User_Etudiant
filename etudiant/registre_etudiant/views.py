from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import  Etudiants
from django.urls import  reverse
from .forms import Etudiantform


def index(request):
    return render(request, 'registre_etudiant/index.html', dict(etudiants=Etudiants.objects.all()))
# Create your views here.

def view_etudiant(request,id):
   # etudiant = Etudiants.objects.get(pk=id)
    return  HttpResponseRedirect(reverse('index'))
def add(request):
  if request.method == 'POST':
    form = Etudiantform(request.POST)
    if form.is_valid():
      new_nom = form.cleaned_data['nom']
      new_prenom = form.cleaned_data['prenom']
      new_email = form.cleaned_data['email']
      new_domaine_etudiant = form.cleaned_data['domaine_etudiant']
      new_code = form.cleaned_data['code']

      new_etudiant = Etudiants(
        nom=new_nom,
        prenom=new_prenom,
        email=new_email,
        domaine_etudiant=new_domaine_etudiant,
        code=new_code
      )
      new_etudiant.save()
      return render(request, 'registre_etudiant/add.html', {
        'form': Etudiantform(),
        'success': True
      })
  else:
    form = Etudiantform
    return render(request, 'registre_etudiant/add.html', {
    'form': Etudiantform

  })

def edit(request, id):
    if request.method == 'POST':
      etudiant = Etudiants.objects.get(pk=id)
      form = Etudiantform(request.POST or None ,instance=etudiant)
      if form.is_valid():
        form.save()
        return render(request, 'registre_etudiant/edit.html', {
          'form': form,
          'success': True
        })
    else:
      etudiant = Etudiants.objects.get(pk=id)
      form = Etudiantform(instance=etudiant)
    return render(request, 'registre_etudiant/edit.html', {
      'form': form
    })

def delete(request, id):
    if request.method == 'POST':
      etudiant = Etudiants.objects.get(pk=id)
      etudiant.delete()
    return HttpResponseRedirect(reverse('index'))






