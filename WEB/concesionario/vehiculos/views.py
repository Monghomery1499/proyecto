from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

# vista basadas en funciones
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/listar_proveedor/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/listar_proveedor/')
        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'login.html', ctx)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def inicio_view(request):
    vehiculos = Vehiculo.objects.all()
    ctx = {'vehiculos': vehiculos}
    return render(request, 'index.html', ctx)


def registrar_view(request):
    info = "inicializar"
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil = Perfil()
            perfil.usuario = user
            perfil.telefono = form.cleaned_data['telefono']
            perfil.direccion = form.cleaned_data['direccion']
            perfil.cedula = form.cleaned_data['cedula']
            perfil.foto = form.cleaned_data['foto']
            perfil.save()
            info = "Usuario Guardado con Exito"
            ctx = {'info': info}
            return render(request, 'registro_ex.html', ctx)
    else:
        form = PerfilForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    ctx = {'form': form, 'info': info}
    return render(request, 'registro_user.html', ctx)


@login_required(login_url='/login/')
def nuevo_view(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        ctx = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('/inicio/')
    else:
        form = VehiculoForm()
        ctx = {'form': form}
    return render(request, 'nuevo.html', ctx)


@login_required(login_url='/login/')
def editar_view(request, id):
    p = Vehiculo.objects.get(id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio/')
        else:
            form = VehiculoForm(instance=p)
    else:
        form = VehiculoForm(instance=p)
    return render(request, 'editar.html', {'p': p, 'form': form})


@login_required(login_url='/login/')
def eliminar_view(request, id):
    car = Vehiculo.objects.get(id=id)
    car.delete()
    return redirect('/inicio/')

#<=============== VISTAS BASADAS EN CLASES ===============================>

class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'plantilla/crear_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')

class listadoProveedor(ListView):
    model = Proveedor
    template_name = 'plantilla/listar_proveedor.html'
    queryset = Proveedor.objects.filter(estado=True)
    context_object_name = 'proveedores'

class ActualizarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'plantilla/editar_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')

class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'plantilla/proveedor_confirm_delete.html'
    def post(self,request,pk,*args,**kwargs):
        object = Proveedor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('listar_proveedor')

