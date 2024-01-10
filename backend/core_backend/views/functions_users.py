from rest_framework import status #codigos de retorno
from rest_framework.response import Response #retorno de la función(json)
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import pdb #donde lo llamemos pausa el código y nos permite utilizar las variables dentro de 

@api_view(['GET']) #decoradores, para reconocer como api
@permission_classes([AllowAny]) #todos los permisos al api
def hello_world(request): #esta recibiendo una petición
    try:
        print('hola, mundo') #todo lo que tiene que hacer nuestra api
        return Response('Este es el response del api') #response_http
    except:
        print('Adios, mundo')
        return Response(status.HTTP_400_BAD_REQUEST)