from django.urls import path
from .views import (crear_profesor, saludo, saludo_con_template, inicio,
                    crear_curso, crear_estudiante,buscar_cursos,curso_1,ver_curso_detail, eliminar_curso, editar_curso,
                     AutoCreateView, AutoListView, AutoDeleteView, AutoDetailView, AutoUpdateView)
urlpatterns = [
   path('',inicio, name= 'inicio'),
   path('hola-mundo/' , saludo),
   path ('hola-mundo-template/' , saludo_con_template),
   path('crear-profesor/',crear_profesor, name='crear-profesor'),
   path('crear-curso/', crear_curso, name= 'curso'),
   path('crear-estudiante/', crear_estudiante, name= 'crear-estudiante'),
   path('cursos/', curso_1, name='cursos'),
   path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
   path('ver_curso/<int:pk>/',ver_curso_detail, name='ver_curso'),
   path('eliminar_curso/<int:pk>/',eliminar_curso, name='eliminar_curso'),
   path('editar_curso/<int:pk>/', editar_curso, name='editar_curso'),
   

  # urls con vistas basadas en clase
   path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
   path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
   path('detalle-auto/<int:pk>', AutoDetailView.as_view(), name='detalle-auto'),
   path('editar/<int:pk>/', AutoUpdateView.as_view(), name='editar-auto'),
   path('eliminar/<int:pk>/', AutoDeleteView.as_view(), name='eliminar-auto'),

   ]