from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('id_usuario', 'nombre', 'apellido', 'correo', 'celular', 'rol')
    search_fields = ('nombre', 'apellido', 'email')


class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('id_usuario', 'nombre', 'apellido', 'correo', 'celular', 'rol')
    search_fields = ('nombre', 'apellido', 'email')


class BarberoAdmin(admin.ModelAdmin):

    list_display = ('id_barbero', 'id_usuario', 'detalle', 'foto')
    search_fields = ('id_usuario', 'detalle')


class CatalogoAdmin(admin.ModelAdmin):

    list_display = ('id_catalogo', 'tipo', 'nombre', 'valor', 'imagen')
    search_fields = ('nombre',)


class HoraAdmin(admin.ModelAdmin):

    list_display = ('id_hora', 'hora')
    list_filter = ('hora',)


class ReservaAdmin(admin.ModelAdmin):

    list_display = ('id_reserva', 'fecha', 'id_hora', 'id_usuario', 'id_barbero', 'id_catalogo')
    search_fields = ('id_usuario', 'id_barbero')
    list_filter = ('id_barbero', 'fecha', 'id_catalogo', 'id_usuario', 'id_hora')  


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Barbero, BarberoAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Hora, HoraAdmin)
admin.site.register(Reserva, ReservaAdmin)
