from django import forms
from .models import Alumno, Grado, Seccion, Inscripcion


class AlumnoForms(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'


class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = '__all__'


class SeccionFrom(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = '__all__'


class InscripcionFrom(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
