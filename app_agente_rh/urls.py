from django.urls import path
from app_agente_rh.views import login, credenciais

urlpatterns = [
    path('', login, name="login"),
    path('resultado/', credenciais, name="resultado")
]