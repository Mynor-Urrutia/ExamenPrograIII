from django import forms
from .models import Alumno, Grado, Seccion

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