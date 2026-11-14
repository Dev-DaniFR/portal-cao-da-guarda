from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('como-ajudar/', views.como_ajudar, name='como_ajudar'),
    path('contato/', views.contato, name='contato'),
    path('adocao/', views.adocao, name='adocao'),
]

