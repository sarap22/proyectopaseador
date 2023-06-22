import json
from typing import Any
from MySQLdb import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from appPaseador.models import *

class getDuenio(View):
    def get(self,request):
        objects= duenio.objects.all().values()
        objectsDuenio=list(objects)
        return JsonResponse(objectsDuenio, safe=False)

class insertDuenio(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            registerInsertDuenio=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'El nombre de usuario ya existe'})
        
        documento=registerInsertDuenio.get('documento')
        user=registerInsertDuenio.get('user')
        nombre=registerInsertDuenio.get('nombre')
        apellido=registerInsertDuenio.get('apellido')
        tel=registerInsertDuenio.get('tel')
        direccion=registerInsertDuenio.get('direccion')
        correo=registerInsertDuenio.get('correo')
        clave=registerInsertDuenio.get('clave')
        rol=registerInsertDuenio.get('rol')
        duenio.objects.create(documento=documento, user=user, nombre=nombre,apellido=apellido,tel=tel,direccion=direccion,correo=correo, clave=clave,rol=rol)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'dueño insertado'})

""" class datosDuenio(View):
    def to_json(self):
        # Lógica para convertir los atributos del objeto en un diccionario
        # o en una estructura de datos compatible con JSON
        return {
            "documento":"documento",
            "user":"user",
            "nombre":"nombre",
            "apellido":"apellido",
            "tel":"tel",
            "direccion":"direccion",
            "correo":"correo",
            "clave":"clave",
            "rol":"rol"
            }
    def get(self,request, pk):
        register= duenio.objects.get(documento=pk)
        registerDuenio= json.dumps(register.to_json())
        return JsonResponse(registerDuenio, safe=False) """
    
class editDuenio(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    
    def put(self, request, pk):
        try:
            pKey=duenio.objects.get(pk=pk)
        
        except duenio.DoesNotExist:
            return JsonResponse({'Error':'El dueño ingresado no existe'})
        data= json.loads(request.body)
        pKey.user=data.get('user')
        pKey.nombre=data.get('nombre')
        pKey.apellido=data.get('apellido')
        pKey.tel=data.get('tel')
        pKey.direccion=data.get('direccion')
        pKey.correo=data.get('correo')
        pKey.clave=data.get('clave')
        pKey.save()
        return JsonResponse({"Mensaje":"Datos actualizados"})


class insertAdmin(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            registerInsertAdmin=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'El nombre de usuario ya existe'})
        
        documento=registerInsertAdmin.get('documento')
        user=registerInsertAdmin.get('user')
        nombre=registerInsertAdmin.get('nombre')
        apellido=registerInsertAdmin.get('apellido')
        correo=registerInsertAdmin.get('correo')
        clave=registerInsertAdmin.get('clave')
        rol=registerInsertAdmin.get('rol')
        administrador.objects.create(documento=documento,user=user, nombre=nombre,apellido=apellido, correo=correo, clave=clave,rol=rol)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'administrador insertado'}) 

class insertPaseador(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            registerInsertPaseador=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'El nombre de usuario ya existe'})
        
        documentoAdmin_id=registerInsertPaseador.get('documentoAdmin_id')
        paseadorUser=registerInsertPaseador.get('paseadorUser')

        adminInsertPaseador.objects.create(documentoAdmin_id=documentoAdmin_id,paseadorUser=paseadorUser)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'paseador insertado'}) 

class insertRegistroPaseador(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            registerValidatePaseador=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'El nombre de usuario ya existe'})
        
        documento=registerValidatePaseador.get('documento')
        user_id=registerValidatePaseador.get('user_id')
        nombre=registerValidatePaseador.get('nombre')
        apellido=registerValidatePaseador.get('apellido')
        tel=registerValidatePaseador.get('tel')
        direccion=registerValidatePaseador.get('direccion')
        correo=registerValidatePaseador.get('correo')
        ocupacion=registerValidatePaseador.get('ocupacion')
        edad=registerValidatePaseador.get('edad')
        clave=registerValidatePaseador.get('clave')
        rol=registerValidatePaseador.get('rol')
        paseador.objects.create(documento=documento, user_id=user_id, nombre=nombre,apellido=apellido,tel=tel,direccion=direccion,correo=correo, ocupacion=ocupacion, edad=edad, clave=clave,rol=rol)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'registro paseador insertado'})

class insertMascota(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            registerMascota=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'no se inserto la mascota'})
        
        nombre=registerMascota.get('nombre')
        raza=registerMascota.get('raza')
        edad=registerMascota.get('edad')
        duenio_id=registerMascota.get('duenio_id')
        mascota.objects.create(nombre=nombre, raza=raza, edad=edad, duenio_id=duenio_id)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'registro mascota insertado'})


class appendCita(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            registerCita=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'los datos son incorrectos'})
    
        precio=registerCita.get('precio')
        lugar=registerCita.get('lugar')
        duenio_id=registerCita.get('duenio_id')
        paseador_id=registerCita.get('paseador_id')
        mascotaId_id=registerCita.get('mascotaId_id')
        cita.objects.create(precio=precio, lugar=lugar, duenio_id=duenio_id, paseador_id=paseador_id, mascotaId_id=mascotaId_id)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'cita agendada'})

class puntajePaseador(View):
    #notacion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            puntaje=json.loads(request.body)

        except IntegrityError:
            return JsonResponse({'error':'los datos son incorrectos'})
    
        puntuacion=puntaje.get('puntuacion')
        duenio_id=puntaje.get('duenio_id')
        paseador_id=puntaje.get('paseador_id')
        calificacion.objects.create(puntuacion=puntuacion, duenio_id=duenio_id, paseador_id=paseador_id)
        #return JsonResponse({'mensaje':'datos guardados'})
        return JsonResponse({'200':'puntuacion realizada'})
