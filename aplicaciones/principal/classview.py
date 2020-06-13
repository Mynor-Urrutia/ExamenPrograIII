from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Alumno
from .models import Grado
from .models import Seccion
from .formEscuela import AlumnoForms, GradoForm, SeccionFrom


class AlumnoList(ListView):
    model = Alumno
    template_name = 'alumnos.html'


class AlumnoCreate(CreateView):
    model = Alumno
    form_class = AlumnoForms
    template_name = 'crearAlumno.html'
    success_url = reverse_lazy('index')


class AlumnoUpdate(UpdateView):
    model = Alumno
    form_class = AlumnoForms
    template_name = 'crearAlumno.html'
    success_url = reverse_lazy('index')


class AlumnosDelete(DeleteView):
    model = Alumno
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class GradoList(ListView):
    model = Grado
    template_name = 'grado.html'


class GradoCreate(CreateView):
    model = Grado
    form_class = GradoForm
    template_name = 'crearGrado.html'
    success_url = reverse_lazy('index')

class GradoUpdate(UpdateView):
    model = Grado
    form_class = GradoForm
    template_name = 'crearGrado.html'
    success_url = reverse_lazy('index')

class SeccionList(ListView):
    model = Seccion
    template_name = 'seccion.html'

class SeccionCreate(CreateView):
    model = Seccion
    form_class = SeccionFrom
    template_name = 'crearSeccion.html'
    success_url = reverse_lazy('index')

class SeccionUpdate(UpdateView):
    model = Seccion
    form_class = SeccionFrom
    template_name = 'crearSeccion.html'
    success_url = reverse_lazy('index')
