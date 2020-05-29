from django.http import HttpResponse
import datetime
from django.template import Template,Context, loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request): # primera vist
    p1 = Persona("Jan","Diaz")
    ahora = datetime.datetime.now()

    # Reemplazado por Loader en settings.py 
    # doc_externo=open("/app/app/views/miPlantilla.html")
    # plantilla = Template(doc_externo.read())
    # doc_externo.close()

    temas= ["covit-19","economia sustentable","Educacion"]

    # ctx = Context({"persona":p1,"momento_actual":ahora,"temas":temas})    
    # documento = plantilla.render(ctx)
    
    # Reemplazado por Render
    # doc_externo = loader.get_template('miPlantilla.html')
    ctx = {"persona":p1,"momento_actual":ahora,"temas":temas}  
    # documento = doc_externo.render(ctx)
    # return HttpResponse(documento)
    return render(request,"miPlantilla.html",ctx)

def curso(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"plantilla_heredada.html",{"dameFecha":fecha_actual})

def curso2(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"plantilla_hija2.html",{"dameFecha":fecha_actual})


def despedida(request):
    return HttpResponse("Hasta luego")

def traer_Fecha(request):
    fecha_actual=datetime.datetime.now()
    documento = "fecha y hora actuales  {0}".format(fecha_actual)
    return HttpResponse(documento)

def calculaedad(request,edad,anno):
    edadActual = edad
    periodo = anno-2020
    edadFutura = edadActual+periodo
    documento = " En el año {0} tendras {1}".format(anno,edadFutura)
    return HttpResponse(documento)