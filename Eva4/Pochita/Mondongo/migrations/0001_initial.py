# Generated by Django 4.2.7 on 2023-12-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('cantidad_notas', models.PositiveSmallIntegerField()),
                ('estado', models.BooleanField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('numero_horas', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=9)),
                ('edad', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('nro_celular', models.CharField(max_length=9)),
                ('direccion', models.TextField()),
                ('ramos_a_cursar', models.ManyToManyField(related_name='estudiante', to='Mondongo.ramo')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=9)),
                ('edad', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('nro_celular', models.CharField(max_length=9)),
                ('direccion', models.TextField()),
                ('ramos_a_impartir', models.ManyToManyField(related_name='docente', to='Mondongo.ramo')),
            ],
        ),
    ]
