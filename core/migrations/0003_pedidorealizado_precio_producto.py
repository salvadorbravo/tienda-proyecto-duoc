# Generated by Django 4.1.7 on 2023-07-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_formulariocontacto_alter_pedidorealizado_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidorealizado',
            name='precio_producto',
            field=models.FloatField(default=0),
        ),
    ]