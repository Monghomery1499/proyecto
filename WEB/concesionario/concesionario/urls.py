"""concesionario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vehiculos.views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inicio"),
    path('logout/', logout_view, name="vista_logout"),
    path('registrar/', registrar_view, name="vista_registrar"),
    path('nuevo/', nuevo_view, name="vista_nuevo"),
    path('editar/<id>/', editar_view, name="vista_editar"),
    path('eliminar/<id>/', eliminar_view, name="vista_eliminar"),

    #º============================URL´S CON VISTAS BASADAS EN CLASES======================================º#
    path('listar_proveedor/',login_required(listadoProveedor.as_view()), name='listar_proveedor'),
    path('crear_proveedor/',login_required(CrearProveedor.as_view()), name='crear_proveedor'),
    path('editar_proveedor/<int:pk>/',login_required(ActualizarProveedor.as_view()), name='editar_proveedor'),
    path('eliminar_proveedor/<int:pk>/',login_required(EliminarProveedor.as_view()), name='eliminar_proveedor'),


    path('', include('vehiculos.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Sistema de Gestion de Vehiculos - Guaman Motors'
