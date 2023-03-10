from datetime import datetime

from django.shortcuts import render

from AppCoder1.models import Curso

def guardarCurso(request):
   # all_cursos = Curso.object.all()
    return render(request, "AppCoder1/cursos.html")



def alumno(request):
    return render(request, "base.html")


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
