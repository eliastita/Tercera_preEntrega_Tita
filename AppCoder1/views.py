from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render, redirect

from AppCoder1.forms import CursoForm, BusqCursoForm, EstudianteForm, BusqEstudianteForm, ProfesorForm, BusqProfesorForm
from AppCoder1.models import Curso, Estudiante, Profesor


def busquedaNombreCurso(request):
    mi_form = BusqCursoForm(request.GET)
    if mi_form.is_valid():
        informacion = mi_form.cleaned_data
        cursos_filtrados = Curso.objects.filter(name__contains=informacion["nombre"])
        contexto = {
            "cursos": cursos_filtrados
        }
        return render(request, "AppCoder1/busquedaCursoNombre.html", context=contexto)


def curso(request):
    all_cursos = Curso.objects.all()
    contexto = {
        "cursos": all_cursos,
        "formsBusqCamada": BusqCursoForm,
    }
    return render(request, "AppCoder1/cursos.html", context=contexto)


def crearCurso(request):
    if request.method == "POST":
        mi_form = CursoForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            curso_save = Curso(name=informacion["nombre"], idc=informacion["camada"])
            curso_save.save()
            return redirect("AppCoder1Curso")

    contexto = {
        "forms": CursoForm(),
    }
    return render(request, "AppCoder1/crearCurso.html", context=contexto)


def eliminarCurso(request, camada):
    get_curso = Curso.objects.get(idc=camada)
    get_curso.delete()
    return redirect("AppCoder1Curso")


def crearCursoURL(request, nombre, idc):
    newcurso = Curso(name=nombre, idc=idc)
    newcurso.save()
    contexto = {
        "nombre": nombre,
        "idc": idc,
    }
    return render(request, "AppCoder1/agregar.html", context=contexto)


def estudiante(request):
    all_estudiante = Estudiante.objects.all()
    contexto = {
        "alumnos": all_estudiante,
        "formsEstudiante": EstudianteForm(),
        "formsBusqEst": BusqEstudianteForm
    }
    return render(request, "AppCoder1/estudiante.html", context=contexto)


def crearEstudiante(request):
    if request.method == "POST":
        mi_form = CursoForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            estudiante_save = Estudiante(apellido=informacion["apellido"], nombre=informacion["nombre"],
                                         email=informacion["email"])
            estudiante_save.save()
            return redirect("AppCoder1Alumno")

    contexto = {
        "forms": EstudianteForm(),
    }
    return render(request, "AppCoder1/crearEstudiante.html", context=contexto)


def busquedaApellidoEstudiante(request):
    if request.method == "POST":
        mi_form = BusqEstudianteForm(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            estudiantes_filtrados = Estudiante.objects.filter(apellido__contains=info["apellido"])
            contexto = {
                "estudiantes": estudiantes_filtrados
            }
            return render(request, "AppCoder1/busquedaEstudiante.html", context=contexto)


def eliminarEstudiante(request, apellido):
    get_estudiante = Estudiante.objects.get(apellido= apellido)
    get_estudiante.delete()
    return redirect("AppCoder1Alumno")


def profesor(request):
    all_profesores = Profesor.objects.all()
    contexto = {
        "profesores": all_profesores,
        "formsProfesor": ProfesorForm,
        "formsBusqProf": BusqProfesorForm
    }
    return render(request, "AppCoder1/profesor.html", context=contexto)


def crearProfesor(request):
    if request.method == "POST":
        mi_form = CursoForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            profesor_save = Profesor(profesion=informacion["profesion"], apellido=informacion["apellido"],
                                     nombre=informacion["nombre"],
                                     email=informacion["email"])
            profesor_save.save()
            return redirect("AppCoder1Profesor")

    contexto = {
        "forms": ProfesorForm(),
    }
    return render(request, "AppCoder1/crearProfesor.html", context=contexto)


def busquedaProfesionProfesor(request):
    if request.method == "POST":
        mi_form = BusqProfesorForm(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            profesor_filtrado = Profesor.objects.filter(profesion__icontains=info["profesion"])
            contexto = {
                "profesores": profesor_filtrado
            }
            return render(request, "AppCoder1/busquedaProfesor.html", context=contexto)

def eliminarProfesor(request, apellido):
    get_profesor = Profesor.objects.get(apellido= apellido)
    get_profesor.delete()
    return redirect("AppCoder1Profesor")

def base_inicio(request):
    return (render(request, "base.html"))
