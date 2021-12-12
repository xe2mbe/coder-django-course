from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

from AppPagina.forms import CursoFormulario
from AppPagina.models import Curso

def inicio(request):

    return render(request, "AppPagina/inicio.html")


def saludo(request):

    return render(request, "AppPagina/saludo.html")

def cursoFormulario(request):
    
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre = informacion['nombre'], comision = informacion['comision'])

            curso.save()

            return render(request, "AppPagina/inicio.html")
    else:

        miFormulario = CursoFormulario()

    return render(request, "AppPagina/cursoFormulario", {"miFormulario":miFormulario})
