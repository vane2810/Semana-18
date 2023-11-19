from django.shortcuts import render
from .models import medico, paciente
from .formularios import add_medic as fm
from .formularios import add_paci as fm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "index.html")

def list_med(request):
    medicos = medico.objects.all()
    return render(request, "lismed.html", {"lismed": medicos})

def add_med(request):
    if request.method == "POST":
        formulario = fm.Add_medic(request.POST)
        if formulario.is_valid():
            nuevoreg = medico()
            nuevoreg.nombre = formulario.data["nombre"]
            nuevoreg.apellido = formulario.data["apellido"]
            nuevoreg.especialidad = formulario.data["especialidad"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.Add_medic()
        return render(request,"Add_medic.html",{"form":formulario})

def add_paciente(request):
    if request.method == "POST":
        formulario = fm.Add_pac(request.POST)
        if formulario.is_valid():
            nuevoreg = paciente()
            nuevoreg.nombre = formulario.data["nombre"]
            nuevoreg.apellido = formulario.data["apellido"]
            nuevoreg.fecha_nacimiento= formulario.data["fecha_nacimiento"]
            nuevoreg.sexo= formulario.data["sexo"]
            nuevoreg.altura = formulario.data["altura"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.Add_pac()
        return render(request,"Add_pac.html",{"form":formulario})
    
def list_paciente(request):
    pacientes = paciente.objects.all()
    return render(request, "lispac.html", {"lispac": pacientes})
