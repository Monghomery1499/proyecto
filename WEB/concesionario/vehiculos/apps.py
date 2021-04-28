from django.apps import AppConfig

class VehiculosConfig(AppConfig):
    name = 'vehiculos'

from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'