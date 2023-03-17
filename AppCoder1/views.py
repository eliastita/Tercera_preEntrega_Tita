from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render, redirect

from AppCoder1.forms import CursoForm, BusqCursoForm
from AppCoder1.models import Curso, Estudiante


def busquedaNombreCurso(request):
    mi_form = BusqCursoForm(request.GET)
    if mi_form.is_valid():
        informacion = mi_form.cleaned_data
        cursos_filtrados= Curso.objects.filter(name__contains=informacion["name"])
        contexto ={
            "cursos":cursos_filtrados
        }

        return render(request, "AppCoder1/busquedaCursoNombre.html", context=contexto)


def curso(request):
    if request.method == "POST":
        mi_form = CursoForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            curso_save = Curso(name=informacion["name"], idc=informacion["idc"])
            curso_save.save()
            return HttpResponse("Curso agregado.")
    all_cursos = Curso.objects.all()
    contexto = {
        "cursos":all_cursos,
        "forms": CursoForm(),
        "formsBusqCamada":BusqCursoForm,
    }
    return render(request, "AppCoder1/cursos.html", context=contexto)

def crearCurso(request, nombre, idc):
    newcurso= Curso(name=nombre,idc= idc)
    newcurso.save()
    contexto = {
        "nombre":nombre,
        "idc":idc,
    }
    return render(request,"AppCoder1/agregar.html", context=contexto)

def estudiante(request):
    all_estudiante = Estudiante.objects.all()
    contexto = {
        "alumnos":all_estudiante
    }
    return render(request, "AppCoder1/estudiante.html", context=contexto)

def base_inicio (request):
    return(render(request, "base.html"))


