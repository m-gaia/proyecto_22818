
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# vista que se encargara de generar logica de negocio
# request -- peticion GET POST etc es un objeto que recibira este metodo hola_mundo
# y contendra informacion de la peticion del cliente - navegador
# metodo hola_mundo
def hola_mundo(request):
    return HttpResponse("Hola Mundo Django 😍")


def saludar(request, nombre='Maru'):
    return HttpResponse(f"""
        <h1>Hola mundo Django - Un gusto {nombre}</h1>
    """)


def ver_proyectos(request, anio, mes):
    return HttpResponse(f"""
        <h1>Proyectos del {mes} / {anio}</h1>
        <p>Listado de proyectos</p>
    """)
