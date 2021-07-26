from django.shortcuts import render
from .models import Automobil, Categoria
# importar modelo de usuarios
from django.contrib.auth.models import User
# importar librerias de acceso a login
from django.contrib.auth import authenticate,logout,login as login_aut
# importar libreria de decorador para impedir el accesos a las paginas
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"index.html")

def galeria(request):
    autos = Automobil.objects.all()
    tipos = Categoria.objects.all()
    contexto = {'registros':autos, "tipos":tipos}
    return render(request,"galeria.html", contexto)

def filtro_tipo(request):
    autos = Automobil.objects.all()
    if request.POST:
        tipo = request.POST.get("cboTipo")
        autos = Automobil.objects.filter(tipo__pk = tipo)
    tipos = Categoria.objects.all()
    contexto = {'registros':autos, "tipos":tipos}
    return render(request,"galeria.html", contexto)

def filtro_palabras(request):
    autos = Automobil.objects.all()
    if request.POST:
        palabras = request.POST.get("txtPalabras")
        automobil = Automobil.objects.filter(descripcion__contains = palabras)
    tipos = Categoria.objects.all()
    contexto = {'registros':autos, "tipos":tipos}
    return render("galeria.html", contexto)

def filtro_id(request,id):
    autos = Automobil.objects.filter(tipo__pk=id)
    tipos = Categoria.objects.all()
    contexto = {'registros':autos, "tipos":tipos}
    return render("galeria.html", contexto)

def somos(request):
    return render(request,"somos.html")

def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")

def login(request):
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=usuario,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request,"index.html")
        else:
            contexto = {"mensaje":"usuario o contraseña incorrecto"}
            return render(request,"login.html",contexto)

    return render(request,"login.html")

def registro(request):
    if request.POST:
        nombre = request.POST.get('txtNombre')
        apellido = request.POST.get('txtApellido')
        mail = request.POST.get('txtEmail')
        nom_usuarui = request.POST.get('txtUsuario')
        pass1 = request.POST.get('txtPassword1')
        pass2 = request.POST.get('txtPassword2')


    return render(request,"registro.html")

# Paginas de admin

def indexadd(request):
    return render(request,"indexadd.html")

@login_required(login_url='/login/')
def newjob(request):
    return render(request,"Newjob.html")

@login_required(login_url='/login/')
def mecanicos(request):
    return render(request,"Mecanicos.html")

@login_required(login_url='/login/')
def asignacion(request):
    return render(request,"asignacion.html")

# paginas de usuario

def indexuser(request):
    return render(request,"indexuser.html")

def galeriau(request):
    return render(request,"galeriau.html")

@login_required(login_url='/login/')
def formulario(request):
    tipos = Categoria.objects.all() #select * from categoria
    contexto = {"tipos":tipos}
    if request.POST:
        patente = request.POST.get("txtPatente")
        annio = request.POST.get("txtAnnio")
        modelo = request.POST.get("txtModelo")
        desc = request.POST.get("txtDesc")
        tipo = request.POST.get("cboTipo")
        imagen = request.FILES.get("txtImg")
        obj_tipo = Categoria.objects.get(nombre=tipo) #recuperando el objeto

        aut = Automobil(
            patente = patente,
            año = annio,
            modelo = modelo,
            descripcion = desc,
            imagen = imagen,
            tipo = obj_tipo
        )
        aut.save()
        contexto = {"tipos":tipos, "mensaje":"grabo"}
        return render(request, "formulario.html",contexto)

    return render(request,"formulario.html", contexto )

def somosu(request):
    return render(request,"somosu.html")

# paginas mecanicos

def indexmec(request):
    return render(request,"indexmec.html")

# mostrar vehiculo

def Autitos(request,id):
    Aut = Automobil.objects.get(patente=id)
    contexto = {"Automobil":Aut}
    return render(request, "Autitos.html", contexto)