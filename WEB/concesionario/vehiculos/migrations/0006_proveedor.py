# Generated by Django 3.0 on 2021-04-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_compra', models.DateTimeField(auto_now=True, verbose_name='Fecha de Compra')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombre'],
            },
        ),
    ]
