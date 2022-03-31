# Generated by Django 4.0.2 on 2022-03-30 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=50)),
                ('genero_mus', models.CharField(max_length=100)),
                ('ritmo', models.CharField(max_length=100)),
                ('dificultad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('contrasena', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=200)),
                ('apellido_p', models.CharField(max_length=100)),
                ('apellido_m', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Historial_partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField()),
                ('tiempo_jugado', models.PositiveIntegerField()),
                ('id_cancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.cancion')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.usuario')),
            ],
        ),
    ]