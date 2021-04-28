from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username','password']

class PerfilForm(UserCreationForm):
    telefono = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    cedula = forms.CharField(widget=forms.TextInput())
    foto = forms.ImageField()

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','propietario','localidad','descripcion']
        labels = {
            'nombre' : 'Nombre de la Empresa',
            'propietario' : 'Ingrese el nombre del gerente',
            'localidad' : 'Ingrese la localidad del proveedor',
            'descripcion' : 'Ingrese una descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre de la empresa',
                    'id' : 'nombre',

                }
            ),
            'propietario': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nomnbre del gerente ',
                    'id' : 'apellido',

                }
            ),
            'localidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la localidad de la empresa',
                    'id' : 'nacionalidad',

                }
            ),
            'descripcion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion',
                    'id' : 'descripcion',

                }
            )
        }


