from django.shortcuts import render
from django.http import HttpResponse #importado manualmente

def login(request):
    return HttpResponse('<h1>Bem-vindo a tela de login.</h1>')