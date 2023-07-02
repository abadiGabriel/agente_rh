from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')

def credenciais(request):
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    html = f"<h1>Usuário: {usuario} </br>Senha:{senha}</h1>"
    return HttpResponse(html)