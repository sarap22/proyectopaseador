from django.db import models

class duenio(models.Model):
    documento= models.CharField(max_length=10, primary_key=True, unique=True)
    user= models.CharField(max_length=30,null=False)
    nombre= models.CharField(max_length=30,null=False)
    apellido= models.CharField(max_length=30,null=False)
    tel= models.PositiveBigIntegerField(verbose_name="telefono", null=False)
    direccion= models.CharField(max_length=30,null=False)
    correo= models.CharField(max_length=30,null=False)
    clave= models.CharField(max_length=30,null=False)
    rol= models.CharField(max_length=5, null=False)


class mascota(models.Model):
    nombre= models.CharField(max_length=30,null=False)
    raza= models.CharField(max_length=30,null=False)
    edad= models.PositiveSmallIntegerField(max_length=2, verbose_name="edad", null=False)
    duenio= models.ForeignKey(duenio, on_delete=models.CASCADE)

class administrador(models.Model):
    documento= models.CharField(max_length=10, primary_key=True, unique=True)
    user= models.CharField(max_length=30,null=False)
    nombre= models.CharField(max_length=30,null=False)
    apellido= models.CharField(max_length=30,null=False)
    correo= models.CharField(max_length=30,null=False)
    clave= models.CharField(max_length=30,null=False)
    rol= models.CharField(max_length=13, null=False)

class adminInsertPaseador(models.Model):
    documentoAdmin=models.ForeignKey(administrador, on_delete=models.CASCADE)
    paseadorUser= models.CharField(max_length=30, primary_key=True, unique=True)

class paseador(models.Model):
    documento= models.CharField(max_length=10, primary_key=True, unique=True)
    user= models.ForeignKey(adminInsertPaseador, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=30,null=False)
    apellido= models.CharField(max_length=30,null=False)
    tel= models.PositiveBigIntegerField(verbose_name="telefono", null=False)
    direccion= models.CharField(max_length=30,null=False)
    correo= models.CharField(max_length=30,null=False)
    ocupacion= models.CharField(max_length=30,null=False)
    edad= models.PositiveSmallIntegerField(max_length=2, verbose_name="edad", null=False)
    clave= models.CharField(max_length=30,null=False)
    rol= models.CharField(max_length=8, null=False)

class cita(models.Model):
    fecha=models.DateField(auto_now_add=True)
    hora=models.TimeField(auto_now=True)
    precio=models.PositiveBigIntegerField(verbose_name="precio")
    lugar= models.CharField(max_length=30,null=False)
    duenio= models.ForeignKey(duenio, on_delete=models.CASCADE)
    paseador= models.ForeignKey(paseador, on_delete=models.CASCADE)
    mascotaId=models.ForeignKey(mascota, on_delete=models.CASCADE)

class calificacion(models.Model):
    puntuacion=models.PositiveSmallIntegerField(max_length=6, verbose_name="puntuacion", null=False)
    duenio= models.ForeignKey(duenio, on_delete=models.CASCADE)
    paseador= models.ForeignKey(paseador, on_delete=models.CASCADE)