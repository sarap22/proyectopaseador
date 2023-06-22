# Generated by Django 4.1.7 on 2023-06-22 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPaseador', '0002_remove_calificacion_duenio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminInsertPaseador',
            fields=[
                ('paseadorUser', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('documento', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=30)),
                ('rol', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='paseador',
            fields=[
                ('documento', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('tel', models.PositiveBigIntegerField(verbose_name='telefono')),
                ('direccion', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('ocupacion', models.CharField(max_length=30)),
                ('edad', models.PositiveSmallIntegerField(max_length=2, verbose_name='edad')),
                ('clave', models.CharField(max_length=30)),
                ('rol', models.CharField(max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.admininsertpaseador')),
            ],
        ),
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now=True)),
                ('precio', models.PositiveBigIntegerField(verbose_name='precio')),
                ('lugar', models.CharField(max_length=30)),
                ('edad', models.PositiveSmallIntegerField(max_length=2, verbose_name='edad')),
                ('duenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.duenio')),
                ('mascotaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.mascota')),
                ('paseador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.paseador')),
            ],
        ),
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.PositiveSmallIntegerField(max_length=6, verbose_name='puntuacion')),
                ('duenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.duenio')),
                ('paseador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.paseador')),
            ],
        ),
        migrations.AddField(
            model_name='admininsertpaseador',
            name='documentoAdmin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPaseador.administrador'),
        ),
    ]