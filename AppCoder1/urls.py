from django.urls import path, include
from AppCoder1 import views

from AppCoder1.views import curso, alumno, base_inicio, crearCurso

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', base_inicio, name="AppCoder1Base"),
    path('curso/', curso, name="AppCoder1Curso"),
    path("alumno/", alumno, name="AppCoder1Alumno"),
    path("guardar/<nombre>/<idc>", crearCurso, name="AppCoder1Guardar")
]

