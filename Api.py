import requests

def getWather(city): #se define como funcion de RETORNO
    url = f'https://es.wttr.in/{city}?format=j1'

    response=requests.get(url) #esperamos almacenar la respuesta, get=obtencion de datos
    weather_dic=response.json() #convertimos a un formato JSON, de modo que sea legible y acceder a diferentes partes de la informacion
    print(weather_dic ['current_condition'][0]['FeelsLikeC']) #limitar a solo un dato

getWather('chicago') 

#Si no aplicamos el JSON, nos da el http:
#200=exitoso con contenido
#201=exitoso sin contenido 
#300=Problemas de servicio
#400=El servidor no puede procesar la solicitud
#500=Problemas de servidor

#api_view=decoradores