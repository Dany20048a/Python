class Empleado:
    def __init__(self,name,salario): #dentro de la misma clase
        self.nombre=name
        self.salario=salario

    def obtener_informacion(self):
        return f"Nombre: {self.nombre},salario: ${self.salario}" #f, adentro lleva variables
    
    def aumentar_salario(self,porcentaje):
        aumento = self.salario*(porcentaje/100)
        self.salario +=aumento
        return f"!Aumento del {porcentaje}% aplicado! Nuevo salario: ${self.salario}"
    
    #Crear instancias de la clase empleado
empleado1 = Empleado("Dany Moran",5000)
empleado2=Empleado("Diego Romo",60000)

#Obtener información de los empleados
print(empleado1.obtener_informacion())
print(empleado2.obtener_informacion())

#Aplicar el aumento de salario al empleado 1
print(empleado1.aumentar_salario(10))

#alumno, 
#id, calif, nombre (atributos )
#metodo estudiar (metodos)
#metodo hacer tarea 
#metodo entrar a clase 
#3 atributos y 3 metodos 