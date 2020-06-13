from django.shortcuts import render, redirect
from .models import Alumno
from .models import Grado
from .models import Seccion
from .models import Inscripcion
from .formEscuela import AlumnoForms, GradoForm, SeccionFrom

def inicio(request):
    return render(request, 'index.html')


"""
def alumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {
        'alumnos': alumnos
    }
    return render(request, 'alumnos.html', contexto)


def crearAlumno(request):
    if request.method == 'GET':
        form = AlumnoForms()
        contexto = {
            'form': form
        }
    else:
        form = AlumnoForms(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crearAlumno.html', contexto)


def editarAlumno(request, id):
    alumnos = Alumno.objects.get(id=id)
    if request.method == 'GET':
        form = AlumnoForms(instance=alumnos)
        contexto = {
            'form': form
        }
    else:
        form=AlumnoForms(request.POST, instance= alumnos)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crearAlumno.html', contexto)
"""


def eliminarAlumno(request, id):
    alumnos = Alumno.objects.get(id=id)
    alumnos.delete()
    return redirect('index')


# -----------------------------------------------------------------------------------------------------------------------
"""
def grados(request):
    grados = Grado.objects.all()
    contexto = {
        'grados': grados
    }
    return render(request, 'grado.html', contexto)


def crearGrados(request):
    if request.method == 'GET':
        form = GradoForm()
        contexto = {
            'form': form
        }
    else:
        form = GradoForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crearGrado.html', contexto)


def editarGrados(request, id):
    grados = Grado.objects.get(id=id)
    if request.method =='GET':
        form = GradoForm(instance=grados)
        contexto = {
            'form': form
        }
    else:
        form=GradoForm(request.POST, instance=grados)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crearGrado.html', contexto)

"""


def eliminarGrados(request, id):
    grados = Grado.objects.get(id=id)
    grados.delete()
    return redirect('index')


# -----------------------------------------------------------------------------------------------------------------------
"""
def seccion(request):
    seccion = Seccion.objects.all()
    contexto = {
        'seccion': seccion
    }
    return render(request, 'seccion.html', contexto)


def crearSeccion(request):
    if request.method == 'GET':
        form = SeccionFrom()
        contexto = {
            'form': form
        }
    else:
        form = SeccionFrom(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crearSeccion.html', contexto)

def editarSeccion(request, id):
    seccion = Seccion.objects.get(id=id)
    if request.method =='GET':
        form = SeccionFrom(instance=seccion)
        contexto={
            'form':form
        }
    else:
        form=SeccionFrom(request.POST, instance=seccion)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crearSeccion.html', contexto)

"""

def eliminarSeccion(request, id):
    seccion = Seccion.objects.get(id=id)
    seccion.delete()
    return redirect('index')

def inscripcion(request):
    return render(request, 'inscripcion.html')


