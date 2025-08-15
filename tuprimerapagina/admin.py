from django.contrib import admin

# Register your models here.

from .models import Profesor, Curso , Estudiante, Auto
register_models= [Profesor, Curso, Estudiante, Auto]
admin.site.register(register_models)
