from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


def url_vehiculo(self, filename):
    ruta = "static/img/Vehiculo/%s/%s" % (self.nombre, str(filename))
    return ruta

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


# Clase Producto en la clase del Inge Yandry
class Vehiculo(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    precio = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=url_vehiculo)

    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def imagen_vehiculo(self):
        return mark_safe(
            '<a href="/%s"> <img src="/%s" height="100px" width="150px"/></a>' % (self.imagen, self.imagen))

    imagen_vehiculo.allow_tags = True

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    cuidad = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100)
    gerente = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    vehiculos = models.ManyToManyField(Vehiculo)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'


def url_perfil(self, filename):
    ruta = "static/img/img_Perfiles/%s/%s" % (self.usuario, str(filename))
    return ruta


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    direccion = models.TextField()
    cedula = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=url_perfil)

    def foto_perfil(self):
        return mark_safe('<a href="/%s"> <img src="/%s" height="100px" width="150px"/></a>' % (self.foto, self.foto))

    foto_perfil.all_tags = True

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.usuario.username

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    propietario = models.CharField(max_length=100)
    localidad = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=200, null=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_compra = models.DateTimeField('Fecha de Compra',auto_now=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre