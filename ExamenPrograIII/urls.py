"""ExamenPrograIII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.principal.views import inicio, eliminarAlumno, eliminarGrados, eliminarSeccion, inscripcion
from aplicaciones.principal.classview import AlumnoList, AlumnoCreate, AlumnoUpdate, GradoList, GradoCreate, GradoUpdate, SeccionList, SeccionCreate, SeccionUpdate, InscripcionList, InscripcionCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('inscripcion/', inscripcion, name='inscripcion'),
    path('alumnos/', AlumnoList.as_view(), name='alumnos'),
    path('crear_alumno/', AlumnoCreate.as_view(), name='crear_alumno'),
    path('editarAlumno/<int:pk>/', AlumnoUpdate.as_view(), name='editarAlumno'),
    path('eliminarAlumno/<int:id>', eliminarAlumno, name='eliminarAlumno'),
    path('grados/', GradoList.as_view(), name='grados'),
    path('crear_grado/', GradoCreate.as_view(), name='crear_grado'),
    path('editarGrado/<int:pk>', GradoUpdate.as_view(), name='editarGrado'),
    path('eliminarGrados/<int:id>', eliminarGrados, name='eliminarGrados'),
    path('seccion/', SeccionList.as_view(), name='seccion'),
    path('crear_seccion/', SeccionCreate.as_view(), name='crear_seccion'),
    path('editarSeccion/<int:pk>', SeccionUpdate.as_view(), name='editarSeccion'),
    path('eliminarSeccion/<int:id>', eliminarSeccion, name='eliminarSeccion'),
    path('InscripcionList/', InscripcionList.as_view(), name='InscripcionList'),
    path('crearInscripcion/', InscripcionCreate.as_view(), name='crearInscripcion')


]
