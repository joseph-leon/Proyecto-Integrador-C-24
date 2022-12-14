from django.contrib import admin

from .models import (
    Usuario, Titulo, Eslogan, Parrafoobjetivos,
    Subobjetivo1, Subobjetivo2, Tec1, Tec2, Tec3, 
    Tec4, Contacto
)

admin.site.register(Usuario)
admin.site.register(Titulo)
admin.site.register(Eslogan)
admin.site.register(Parrafoobjetivos)
admin.site.register(Subobjetivo1)
admin.site.register(Subobjetivo2)
admin.site.register(Tec1)
admin.site.register(Tec2)
admin.site.register(Tec3)
admin.site.register(Tec4)
admin.site.register(Contacto)