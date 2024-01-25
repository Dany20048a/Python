from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Reservacion, Sala, Usuario
from voluptuous.schema_builder import Required
from backend.utils import validate_data
from datetime import datetime,date,time
from unidecode import unidecode
from django.utils.text import slugify

@api_view(['GET'])
@permission_classes([AllowAny])
def get_reservation(request):
     reservaciones = Reservacion.objects.all()
     response = []
     for reservacion in reservaciones:
      try:
            #'apellido': slugify(unidecode(reservacion.usuario.apellido)).capitalize() if reservacion.usuario else None,
            #'identificador': reservacion.usuario.identificador if reservacion.usuario else None
        response.append({
            'id': reservacion.id,
            'usuario': slugify(unidecode(reservacion.usuario.nombre)).capitalize() if reservacion.usuario else None,
            'sala': slugify(unidecode(reservacion.sala.nombre)).capitalize() if reservacion.sala else None,
            'fecha': reservacion.fecha,
            'hora inicio': reservacion.hora_inicio,
            'hora final':reservacion.hora_final,
            'personas':reservacion.personas
        })
      except:
         return Response('Error al procesar la reservación')
     return Response(response)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_reservationUser(request):
    data = validate_data({
        Required('nombre'): str,
    }, request.data)
    reservaciones = Reservacion.objects.filter(usuario__nombre__iexact=data['nombre'])
    response = []
    for reservacion in reservaciones:
      try:
        response.append({
            'id': reservacion.id,
            'usuario': slugify(unidecode(reservacion.usuario.nombre)).capitalize() if reservacion.usuario else None,
            'sala': slugify(unidecode(reservacion.sala.nombre)).capitalize() if reservacion.sala else None,
            'fecha': reservacion.fecha,
            'hora inicio': reservacion.hora_inicio,
            'hora final':reservacion.hora_final,
            'personas':reservacion.personas
        })
      except:
        return Response('Usuario no encontrado')
    return Response(response)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation(request):
     data = validate_data({
        Required('identificador'):int,
        Required('personas'):int,
        Required('fecha'):str,
        Required('sala'):str,
        Required('hora_inicio'):str,
        Required('hora_final'):str
    },request.data)
     data['fecha'] = datetime.strptime(data['fecha'], '%Y-%m-%d').date()     
     data['hora_inicio'] = datetime.strptime(data['hora_inicio'], '%H:%M:%S').time()     
     data['hora_final'] = datetime.strptime(data['hora_final'], '%H:%M:%S').time()
     try: 
         sala=Sala.objects.get(nombre=data['sala'])
         if sala.aforo is not None and data['personas']>sala.aforo:
             return Response('La cantidad de personas supera el aforo de la sala')
         reservaciones = Reservacion.objects.filter()
         for reservacion in reservaciones:
            if(reservacion.fecha == data['fecha']):
                if (reservacion.hora_inicio < data['hora_final'] and reservacion.hora_final > data['hora_inicio']) or \
                (reservacion.hora_inicio == data['hora_inicio'] and reservacion.hora_final == data['hora_final']) or \
                (reservacion.hora_inicio > data['hora_inicio'] and reservacion.hora_final < data['hora_final']):
                 return Response ('La nueva reservación se empalma con una reservación existente')
                if ((datetime.combine(datetime.min, data['hora_final']) - datetime.combine(datetime.min, data['hora_inicio'])).total_seconds() / 3600) > 2:
                 return Response('La nueva reservación supera el límite de tiempo')
     except Sala.DoesNotExist: 
         return Response('Sala inexistente')
     try:
        user = Usuario.objects.get(identificador=data['identificador'])
     except Usuario.DoesNotExist:
        return Response('Usuario inexistente')
     cita = Reservacion.objects.create(sala=sala,fecha=data['fecha'],hora_inicio=data['hora_inicio'],hora_final=data['hora_final'],personas=data['personas'],usuario=user)
     cita.save()
     return Response('Reservación creada con éxito')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_reservation(request):
    data = validate_data({
        Required('id'):int,
        ('personas'):int,
        ('fecha'):str,
        ('hora_inicio'):str,
        ('hora_final'):str,
        ('sala'):str
    },request.data)
    try:
        sala = Sala.objects.get(nombre=data['sala'])
        if 'personas' in data and sala.aforo is not None and data['personas']>sala.aforo:
           return Response('La cantidad de personas actualizada supera el aforo de la sala')
        if 'hora_inicio' in data and 'hora_final' in data:
           data['hora_inicio'] = datetime.strptime(data['hora_inicio'], '%H:%M:%S').time()
           data['hora_final'] = datetime.strptime(data['hora_final'], '%H:%M:%S').time()
           reservaciones = Reservacion.objects.filter()
           for reservacion in reservaciones:
            if (reservacion.hora_inicio < data['hora_final'] and reservacion.hora_final > data['hora_inicio']) or \
               (reservacion.hora_inicio == data['hora_inicio'] and reservacion.hora_final == data['hora_final']) or \
               (reservacion.hora_inicio > data['hora_inicio'] and reservacion.hora_final < data['hora_final']):
               return Response ('La reservación actualizada se empalma con una reservación existente')
            if (
                    (datetime.combine(datetime.min, data['hora_final']) - datetime.combine(datetime.min, data['hora_inicio'])).total_seconds() / 3600 > 2
                ):
                    return Response('La reservación actualizada supera el límite de tiempo')
        reservacion = Reservacion.objects.get(id = data['id'])
        if 'personas' in data:
            reservacion.personas = data['personas']
        if 'fecha' in data:
            reservacion.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
        if 'hora_inicio' in data:
            reservacion.hora_inicio = data['hora_inicio']
        if 'hora_final' in data:
            reservacion.hora_final = data['hora_final']
        if 'sala' in data: 
            Sala.sala = data['sala']
        reservacion.save()
        return Response('Reservación actualizada exitosamente')
    except Sala.DoesNotExist:
        return Response('La sala no existe') 
    except Reservacion.DoesNotExist:
        return Response('La reservación no existe')

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_reservation(request):
    data = validate_data({
        Required('id'):int,
    }, request.data)
    try:
        reservacion = Reservacion.objects.get(id=data['id'])
        reservacion.delete()
        return Response('Reservación eliminada exitosamente')
    except:
        return Response('La reservación que deseas eliminar no existe')
     