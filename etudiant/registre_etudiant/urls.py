from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_etudiant, name ='view_etudiant'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),




]