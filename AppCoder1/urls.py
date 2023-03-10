from django.urls import path, include
from AppCoder1 import views

from AppCoder1.views import guardarCurso, alumno
from AppCoder1.views import pagina_inicio, hora

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('saludo/<nombre>', pagina_inicio),
    path('', hora),
    path('curso/', guardarCurso),
    path("alumno/", alumno)
]

