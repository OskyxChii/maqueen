from django.contrib import admin
from django.urls import path
from .views import cerrar_sesion, Autitos, index, galeria, indexmec, somos, login,registro, indexadd, mecanicos, asignacion, newjob, indexuser, galeriau, formulario, somosu, indexmec, Autitos, filtro_tipo, filtro_id, filtro_palabras

urlpatterns = [
    path('',index,name="ind"),
    path('galeria/',galeria,name="gal"),
    path('somos/',somos,name="som"),
    path('login/',login,name="log"),
    path('login/Registro/',registro,name="reg"),
    path('indexadd/',indexadd,name="inda"),
    path('Newjob/',newjob,name="nj"),
    path('Mecanicos/',mecanicos,name="meca"),
    path('asignacion/',asignacion,name="asig"),
    path('indexuser/',indexuser,name="indu"),
    path('galeriau/',galeriau,name="galu"),
    path('formulario/',formulario,name="for"),
    path('somosu/',somosu,name="somu"),
    path('indexmec',indexmec,name="indm"),
    path('Autitos/<id>/', Autitos,name="mostrarv"),
    path('filtro_tipo', filtro_tipo,name="filtrot"),
    path('filtro_id/<id>', filtro_id,name="filtroid"),
    path('filtro_palabras', filtro_palabras,name="filtropa"),
    path('cerrar/', cerrar_sesion, name="cerrar")
]