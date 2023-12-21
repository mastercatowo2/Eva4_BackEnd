from django.contrib import admin

from Mondongo.models import Estudiante
from Mondongo.models import Docente
from Mondongo.models import Ramo

# https://copyprogramming.com/howto/getting-the-error-class-blog-app-admin-requestdemoadmin-admin-e109-the-value-of-list-display-6-must-not-be-a-manytomanyfield


# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'edad', 'email', 'nro_celular', 'direccion', 'display_ramos_a_cursar']

    def display_ramos_a_cursar(self, obj):
        return ", ".join([ramo.nombre for ramo in obj.ramos_a_cursar.all()])
    display_ramos_a_cursar.short_description = 'Ramos a Cursar'

admin.site.register(Estudiante, EstudianteAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'edad', 'email', 'nro_celular', 'direccion', 'display_ramos_a_impartir']

    def display_ramos_a_impartir(self, obj):
        return ", ".join([ramo.nombre for ramo in obj.ramos_a_impartir.all()])
    display_ramos_a_impartir.short_description = 'Ramos a Impartir'

admin.site.register(Docente, DocenteAdmin)


class RamoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_notas', 'estado', 'fecha_inicio', 'fecha_termino', 'numero_horas']

admin.site.register(Ramo, RamoAdmin)

