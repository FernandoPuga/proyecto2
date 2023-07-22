from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse ("Hola Mundo!!!!")

def bienvenida(request):
    return HttpResponse ("<html><h1>Bienvenidos a Django con Python!!</h1></html>") #<html> es como un print y <h1> hace referencia al tamaño de la letra

def diaDeHoy(request):
    dia = datetime.datetime.now()
    respuestaDia = f"Hoy es : <br> {dia}" #el <br> es para saltar de renglon
    return HttpResponse (respuestaDia)

def saludoPersonal(request,nombre):
    saludo = f"Bienvenido {nombre}!!!"
    return HttpResponse(saludo)


def pruebaTemplate(request):

    plantilla = loader.get_template("index.html")

    datos = {
            "nombre" : "fernando",
            "apellido" : "puga",
            "dni" : 123456,
            "fecha" : datetime.datetime.now(),
            "notas" : [7,8,10,2,4,3],
    }
        
    documento = plantilla.render(datos)
    return HttpResponse(documento)
     


