from django.urls import path
from .views import functions_usuario

users_url = [
   path('create_users',functions_usuario.create_users,name='create_users'), #name=hello (endpoints)
   path('get_users',functions_usuario.get_users,name='get_users'),
   path('get_usersid',functions_usuario.get_usersid,name='get_usersid'),
   path('update_users',functions_usuario.update_users,name='update_users'),
   path('delete_users',functions_usuario.delete_users,name='delete_users')
   #Nombre de la aplicación
]

urlpatterns = users_url 