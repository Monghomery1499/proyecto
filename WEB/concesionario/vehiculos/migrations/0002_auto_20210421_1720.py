# Generated by Django 3.0 on 2021-04-21 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='decripcion',
            new_name='descripcion',
        ),
    ]