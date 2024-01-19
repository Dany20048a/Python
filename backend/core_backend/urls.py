from django.urls import path
from .views import functions_usuario,functions_reservation,functions_room

users_url = [
   path('create_users',functions_usuario.create_users,name='create_users'), #name=hello (endpoints)
   path('get_users',functions_usuario.get_users,name='get_users'),
   path('get_usersid',functions_usuario.get_usersid,name='get_usersid'),
   path('update_users',functions_usuario.update_users,name='update_users'),
   path('delete_users',functions_usuario.delete_users,name='delete_users'),
   #Nombre de la aplicación
]
reservations_url = [
   path('create_reservation',functions_reservation.create_reservation,name='create_reservation'),
   path('get_reservation',functions_reservation.get_reservation,name='get_reservation'),
   path('update_reservation',functions_reservation.update_reservation,name='update_reservation'),
   path('delete_reservation',functions_reservation.delete_reservation,name='delete_reservation'),
]
rooms_url = [
   path('create_room',functions_room.create_room,name='create_room'),
   path('get_room',functions_room.get_rooms,name='get_room'),
   path('update_room',functions_room.update_room,name='update_room'),
   path('delete_room',functions_room.delete_room,name='delete_room'),
   path('get_reservationUser',functions_reservation.get_reservationUser,name='get_reservationUser')
]
urlpatterns = users_url + reservations_url + rooms_url