from random import randint
from django.test import TestCase
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from animaissos.views import index
from django.urls import resolve
import random
from app_animais.views import getCampanhas, getCampanhasAtivas, registerCampaign
# Create your tests here.

class TestApp(TestCase):

    # testa se página inicial está sendo resolvida
    def test_index(self):
        root = resolve('/')
        self.assertEqual(root.func,index)
    
    # testa chamadas relacionadas as rotas das campanhas
    def test_campanhas(self):
        campanha_ativa = resolve('/campanha/ativa/')
        self.assertEqual(campanha_ativa.func, getCampanhasAtivas)
        campanha_lista = resolve('/campanha/listar/')
        self.assertEqual(campanha_lista.func, getCampanhas)
        numero = random.randint(1,10)
        campanha_iniciar = resolve(f'/campanha/iniciar/{numero}')
        self.assertEqual(campanha_iniciar.func, registerCampaign )