from io import UnsupportedOperation
from flask import render_template, request
from gc import get_objects
from re import L
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from spotifyTry.forms import FormPersona

from spotifyTry.models import Ciudad, Persona, TipoDocumento
import json

# Create your views here.


def index(request):
    error = False
    if request.method == 'POST':
        form = FormPersona(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            error = True
            print(form.errors)

    personasListadas = Persona.objects.all()
    ciudades = Ciudad.objects.all()
    Tipo = TipoDocumento.objects.all()
    return render(
        request, "paginas/inicio.html", {
            "personas": personasListadas,
            "ciudades": ciudades,
            "Tipo": Tipo,
            "error": error
        })


def edicionPersonas(request, id):
    personas = Persona.objects.get(id=id)
    #personasListadas = Persona.objects.all()
    ciudades = Ciudad.objects.all()
    Tipo = TipoDocumento.objects.all()
    return render(
        request,
        "edicionPersonas.html",
        {
            "p": personas,
            #"personas": personasListadas,
            "ciudades": ciudades,
            "Tipo": Tipo
        })


def eliminacionPersonas(request, usuario):
    personas = Persona.objects.get(usuario=usuario)
    personas.delete()
    return redirect('/')


def editarPersonas(request, id):
    if request.method == 'POST':
        persona = get_object_or_404(Persona, id=id)
        form = FormPersona(request.POST, request.FILES, instance=persona)

        if form.is_valid():
            print("aca2")

            persona.nombre = form.cleaned_data.get("nombres")
            persona.apellido = form.cleaned_data.get("apellidos")
            persona.tipodocumento = form.cleaned_data.get("tipodocumento")
            persona.lugarderecidencia = form.cleaned_data.get(
                "lugarderecidencia")
            persona.fechadenacimiento = form.cleaned_data.get(
                "fechadenacimiento")
            persona.email = form.cleaned_data.get("email")
            persona.usuario = form.cleaned_data.get("usuario")
            persona.telefono = form.cleaned_data.get("telefono")
            persona.password = form.cleaned_data.get("password")
            persona.save()
            return redirect('/')


def userPersona(req: HttpRequest, usuario):
    print("%s HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEYS" % usuario)
    persona = get_object_or_404(Persona, pk=usuario)
    if req.method == "POST":
        return HttpResponse("este es el usuario que buscabas %s" % persona)
    elif req.method == "DELETE":
        username = persona.usuario
        persona.delete()
        return HttpResponse("usuario %s borrado" % username)
    return


def updatePersona(req: HttpRequest, usuario):
    persona = get_object_or_404(Persona, pk=usuario)
    #persona.nombres = "Juan"
    #persona.save()
    parsed = json.loads(req.body)
    for trait, value in parsed.items():
        try:
            setattr(persona, trait, value)
        except Exception:
            print(Exception)
    persona.save()
    print(persona)
    return HttpResponse("Garcias " + str(req.read()))


def createPersona(req: HttpRequest):
    persona = Persona()
    parsed = json.loads(req.body)
    for trait, value in parsed.items():
        try:
            if (trait == "tipodocumento" or trait == "lugarderecidencia"):
                if (trait == "tipodocumento"):
                    print("documento")
                    documento = TipoDocumento()
                    for trait, value in value.items():
                        setattr(documento, trait, value)
                    documento.save()
                    setattr(persona, "tipodocumento", documento)
                else:
                    print("ciudad")
                    ciudad = Ciudad()
                    for trait, value in value.items():
                        setattr(ciudad, trait, value)
                    ciudad.save()
                    setattr(persona, "lugarderecidencia", ciudad)
            setattr(persona, trait, value)
        except BaseException as e:
            print(e)
    persona.save()
    return HttpResponse("persona creada " + str(persona))


def getDocumento(req: HttpRequest, id):
    documento = get_object_or_404(TipoDocumento, id=id)
    return HttpResponse("Tipo de Documento que busca " + str(documento))
