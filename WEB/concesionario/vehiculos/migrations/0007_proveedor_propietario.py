# Generated by Django 3.0 on 2021-04-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0006_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='propietario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
