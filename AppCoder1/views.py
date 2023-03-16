from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

from AppCoder1.forms import CursoForm
from AppCoder1.models import Curso

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
        "forms": CursoForm()
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

def alumno(request):
    return render(request, "AppCoder1/alumno.html")

def base_inicio (request):
    return(render(request, "base.html"))


