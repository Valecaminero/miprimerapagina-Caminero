from django.contrib import admin

# Register your models here.

from .models import Profesor, Curso , Estudiante
register_models= [Profesor, Curso, Estudiante]
admin.site.register(register_models)
