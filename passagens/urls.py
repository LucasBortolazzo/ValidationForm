from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('minha_passagem', views.minha_passagem, name = 'minha_passagem')
]