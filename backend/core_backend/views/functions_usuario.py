from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Usuario
from voluptuous.schema_builder import Required
from backend.utils import validate_data
import random


@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):
     users = Usuario.objects.all()
     response = []
     for user in users:
        response.append({
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'identificador': user.identificador,
        })
     return Response(response)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_usersid(request):
    data = validate_data({
        Required('id'): int,
    }, request.data)
    try:
        user = Usuario.objects.get(id=data['id'])
        response = {
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'identificador': user.identificador,
        }
        return Response(response)
    except:
        return Response('Usuario no encontrado')
    
@api_view(['POST'])
@permission_classes([AllowAny])
def create_users(request):
    data = validate_data({
        Required('nombre'):str,
        ('apellido'):str,
    },request.data)
    if 'apellido' not in data:
        data['apellido'] = None
    user = Usuario.objects.create(nombre=data['nombre'],apellido=data['apellido'])
    user.identificador = random.randint(1000,9999)
    user.save()
    return Response('Usuario creado con éxito')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_users(request):
    data = validate_data({
        Required('id'):int,
        ('nombre'):str,
        ('apellido'):str,
    },request.data)
    try:
        user = Usuario.objects.get(id = data['id'])
        if 'nombre' in data:
            user.nombre = data['nombre']
        if 'apellido' in data:
            user.apellido = data['apellido']
        user.save()
        return Response('Usuario actualizado exitosamente')
    except:
        return Response('El usuario que deseas modificar no existe') 
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_users(request):
    data = validate_data({
        Required('id'):int,
    }, request.data)
    try:
        user = Usuario.objects.get(id=data['id'])
        user.delete()
        return Response('Usuario eliminado exitosamente')
    except:
        return Response('El usuario que deseas eliminar no existe')