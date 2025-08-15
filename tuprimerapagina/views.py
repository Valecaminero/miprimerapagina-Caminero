from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Curso, Estudiante, Profesor, Auto
# Create your views here.
from django.http import HttpResponse
from .forms import cursoform, EstudianteForm, ProfesorForm, AutoForm, CursoForm
from django.contrib.auth.decorators import login_required

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


@login_required
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
       
def curso_1(request):
   # cursos = Curso.objects.all()
    # Muestra solo los cursos que están "activos"
    cursos = Curso.objects.all()
    return render(request, 'tuprimerapagina/cursos.html', {'cursos': cursos})

@login_required
def ver_curso_detail(request, pk):
    # Obtiene el objeto Curso con el ID=pk o devuelve un 404 si no existe
    curso= get_object_or_404(Curso, pk=pk)
    return render(request, 'tuprimerapagina/ver_curso.html', {'curso': curso})

@login_required
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')
    return redirect('cursos')
      

def buscar_cursos(request):
    if request.method == 'GET':
                nombre= request.GET.get('nombre','')
                cursos= Curso.objects.filter(nombre__icontains=nombre)
                return render(request, 'tuprimerapagina/cursos.html', {'cursos': cursos, 'nombre': nombre})

class AutoListView(ListView):
    model = Auto 
    template_name = 'tuprimerapagina/listar_autos.html'
    context_object_name = 'autos'


class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'tuprimerapagina/crear_auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'tuprimerapagina/detalle_auto.html'
    context_object_name = 'auto'


class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'tuprimerapagina/crear_auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'tuprimerapagina/eliminar_auto.html'
    success_url = reverse_lazy('listar-autos')


@login_required
def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')  # Redirige a la lista de cursos
    else:
        form = CursoForm(instance=curso)  # Muestra el formulario con los datos existentes

    return render(request, 'tuprimerapagina/editar_curso.html', {'form': form, 'curso': curso})