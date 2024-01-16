from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Reservacion
from voluptuous.schema_builder import Required
from backend.utils import validate_data
from datetime import datetime,date,time

@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation(request):
     data = validate_data({
        Required('id'):int,
        Required('fecha'):date,
        Required('sala'):str,
        Required('hora_inicio'):time,
        Required('hora_final'):time
    },request.data)
     sala=sala.objects.get(nombre=data['nombre'])
    # cita=Reservacion.objects.filter(fecha=data['fecha'],sala=sala.id)
     cita=Reservacion.objects.filter(fecha=date.today(),sala=3) #now
     print(cita)
     