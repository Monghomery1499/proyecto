# Generated by Django 3.0 on 2021-04-22 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_auto_20210421_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='almacen',
            options={'verbose_name': 'Almacen', 'verbose_name_plural': 'Almacenes'},
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name': 'Vehiculo', 'verbose_name_plural': 'Vehiculos'},
        ),
    ]