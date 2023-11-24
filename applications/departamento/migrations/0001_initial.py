# Generated by Django 4.2.7 on 2023-11-24 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, verbose_name='Nombre Corto')),
                ('anulate', models.BooleanField(default=True, verbose_name='Anulado')),
            ],
        ),
    ]