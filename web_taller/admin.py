from django.contrib import admin
from django.db import models
from .models import Automobil, Categoria, Sliderindex
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Sliderindex)
admin.site.register(Automobil)