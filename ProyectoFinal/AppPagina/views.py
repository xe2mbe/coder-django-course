from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

def inicio(request):

    return render(request, "AppPagina/inicio.html")


def saludo(request):

    return render(request, "AppPagina/saludo.html")