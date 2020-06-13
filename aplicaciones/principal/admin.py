from django.contrib import admin
from .models import Alumno
from .models import Grado
from .models import Seccion

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Grado)
admin.site.register(Seccion)
