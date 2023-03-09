import random
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from AppCoder1.models import Curso

def guardarCurso(request, nombre):
    curso = Curso(nombre="Java", numero=2)
    curso.save()
    contexto = {
        "nombre" : nombre,
        "numero" : random.randint(0,999)
    }
    return render(request, "curso.html",context= contexto)



def alumno(request):
    return render(request, "index.html")


def pagina_inicio(request, nombre):
    contexto = {
        "nombre":nombre,
        "guess":"Sofia"
    }
    return render(request, "saludo.html", context= contexto)

def hora(request):
    contexto = {
        "fecha" : datetime.now()
    }
    return render(request, "inicio.html", context=contexto)
