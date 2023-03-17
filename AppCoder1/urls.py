from django.urls import path, include
from AppCoder1 import views

from AppCoder1.views import curso, estudiante, base_inicio, crearCurso,  busquedaNombreCurso

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', base_inicio, name="AppCoder1Base"),
    path('busqCurso/', busquedaNombreCurso, name="AppCoderBusqCurso"),
    path('curso/', curso, name="AppCoder1Curso"),
    path("alumno/", estudiante, name="AppCoder1Alumno"),
    path("guardar/<nombre>/<idc>", crearCurso, name="AppCoder1Guardar")
]

