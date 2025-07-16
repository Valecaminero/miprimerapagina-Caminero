from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor
# Create your views here.
from django.http import HttpResponse
from .forms import cursoform, EstudianteForm, ProfesorForm

def inicio(request):
       return render(request, 'tuprimerapagina/inicio.html', {})
def saludo(request): 
        return HttpResponse("¡Hola, Mundo!")

def saludo_con_template(request):
        return render(request, 'tuprimerapagina/saludo.html',{})

def crear_profesor(request):
        if request.method== 'POST':
                form = ProfesorForm(request.POST)
                if form.is_valid ():
                # Procesar el formulario y guardar el curso
                        nuevo_profesor = Profesor(
                                nombre=form.cleaned_data['nombre'],
                                apellido=form.cleaned_data['apellido'],
                                email=form.cleaned_data['email'],
                                edad=form.cleaned_data['edad'],
                                fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
                        )
                        nuevo_profesor.save()
                        return redirect('inicio')
        else:
              form = ProfesorForm()
              return render(request, 'tuprimerapagina/crear_profesor.html', {'form': form})


def crear_curso(request):
        if request.method== 'POST':
                form = cursoform(request.POST)
                if form.is_valid():
                # Procesar el formulario y guardar el curso
                        nuevo_curso = Curso(
                                nombre=form.cleaned_data['nombre'],
                                descripcion=form.cleaned_data['descripcion'],
                                duracion_semanas=form.cleaned_data['duracion_semanas'],
                                fecha_inicio=form.cleaned_data['fecha_inicio'],
                                activo=form.cleaned_data['activo']
                        )
                        nuevo_curso.save()
                        return redirect('cursos')
        else:
                form = cursoform()
                return render(request, 'tuprimerapagina/crear_curso.html', {'form': form})


def crear_estudiante(request):
       if request.method == 'POST':
                form = EstudianteForm(request.POST)
                if form.is_valid():
                        # Procesar el formulario y guardar el curso
                        nuevo_estudiante = Estudiante(
                                nombre=form.cleaned_data['nombre'],
                                apellido=form.cleaned_data['apellido'],
                                email=form.cleaned_data['email'],
                                edad=form.cleaned_data['edad'],
                                fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
                        )
                        nuevo_estudiante.save()
                        return redirect('inicio')
       else:
              form = EstudianteForm()
              return render(request, 'tuprimerapagina/crear_estudiante.html', {'form': form})
       
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'tuprimerapagina/cursos.html', {'cursos': cursos})


def buscar_cursos(request):
    if request.method == 'GET':
                nombre= request.GET.get('nombre','')
                cursos= Curso.objects.filter(nombre__icontains=nombre)
                return render(request, 'tuprimerapagina/cursos.html', {'cursos': cursos, 'nombre': nombre})

