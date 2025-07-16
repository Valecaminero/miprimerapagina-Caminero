from django.urls import path
from .views import crear_profesor, saludo, saludo_con_template, inicio,crear_curso, crear_estudiante,buscar_cursos,cursos
urlpatterns = [
   path('',inicio, name= 'inicio'),
   path('hola-mundo/' , saludo),
   path ('hola-mundo-template/' , saludo_con_template),
   path('crear-profesor/',crear_profesor, name='crear-profesor'),
   path('crear-curso/', crear_curso, name= 'curso'),
   path('crear-estudiante/', crear_estudiante, name= 'crear-estudiante'),
   path('cursos/', cursos, name='cursos'),
   path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
   ]