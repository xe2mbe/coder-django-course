from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

def saludo(request):

    plantilla = loader.get_template('template.html')
    dicc ={}

    documento = plantilla.render(dicc)
	
    return HttpResponse(documento)


def diaDeHoy(request):

    dia = datetime.now()

    documentoDeTexto = f"hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)
