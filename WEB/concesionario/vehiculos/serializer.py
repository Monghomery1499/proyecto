from rest_framework import serializers
from .models import *

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


