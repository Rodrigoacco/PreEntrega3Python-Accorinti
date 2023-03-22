from datetime import datetime as dt
from django.template import Template, Context, loader
from django.http import HttpResponse

def saludo (request):
    return HttpResponse("hola")

def dia(request):
    hoy=dt.now()
    return HttpResponse(f"el dia de hoy es: {hoy}")

def probandoTemplate(request):
    
    mis_datos = {"nombre": "Esteban"}
    # mihtml = open("./templates/template1.html")
    # plantilla = Template(mihtml.read())
    # mihtml.close()
    
    plantilla = loader.get_template("template1.html")

    # mi_contexto = Context()

    documento = plantilla.render(mis_datos)
    return HttpResponse(documento)