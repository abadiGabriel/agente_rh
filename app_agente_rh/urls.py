from django.urls import path
from app_agente_rh.views import login

urlpatterns = [
    path('', login),
]