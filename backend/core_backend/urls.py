from django.urls import path
from .views import functions_users

users_url = [
   path('hello_world',functions_users.hello_world,name='hello_world'), #name=hello (endpoints)
   #Nombre de la aplicación
]

urlpatterns = users_url 