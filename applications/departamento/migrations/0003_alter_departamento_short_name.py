# Generated by Django 4.2.7 on 2023-11-25 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_anulate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
