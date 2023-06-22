from django.urls import path
from .views import *

urlpatterns=[
    path('insertDuenio', insertDuenio.as_view(), name='insertDuenio'),
    path('getDuenio', getDuenio.as_view(), name='getDuenio'),
    path('editDuenio/<pk>', editDuenio.as_view(), name='editDuenio'),
    path('insertAdmin', insertAdmin.as_view(), name='insertAdmin'),
    path('insertPaseador', insertPaseador.as_view(), name='insertPaseador'),
    path('insertRegistroPaseador', insertRegistroPaseador.as_view(), name='insertRegistroPaseador'),
    path('insertMascota', insertMascota.as_view(), name='insertMascota'),
    path('appendCita', appendCita.as_view(), name='appendCita'),
    path('puntuacion', puntajePaseador.as_view(), name='puntuacion'),
]