from django.shortcuts import render
from .models import Genero , Alumno

# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def crud(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,"alumnos/alumnos_list.html",context)

def alumnosAdd(request):
    return "hola"

def alumnos_del(request,pk):
    return "hola"

def alumnos_findEdit(request,pk):
    return "Hola"