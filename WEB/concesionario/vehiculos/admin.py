from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VehiculoResource(resources.ModelResource):
    class Meta:
        model = Vehiculo

class VehiculoAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio', 'descripcion', 'fk_categoria', 'imagen_vehiculo')
    search_fields = ['nombre']
    resources_class = VehiculoResource

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ['nombre']


class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'gerente', 'cuidad', 'direccion', 'email')
    search_fields = ['nombre', 'gerente_username']


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'usuario', 'telefono', 'direccion', 'foto_perfil')
    search_fields = ['cedula', 'usuario']

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','propietario','localidad','descripcion','estado', 'fecha_compra')
    search_fields = ['nombre']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Proveedor, ProveedorAdmin)