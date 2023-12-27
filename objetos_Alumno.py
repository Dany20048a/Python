class Alumno: 
    def __init__(self,nombre,id_alu,calif,materias=None,tareas=None):
        self.nombre=nombre
        self.id=id_alu
        self.calif=calif
        self.materias=materias if materias else [] #lista
        self.tareas=tareas if tareas else {} #diccionario tarea-materia (clave-valor)

    def obtener_informacion(self):
        return f"Nombre: {self.nombre},ID {self.id},calificación: {self.calif}"
    
    def estudiar(self,materias):
        self.materias=materias
        return f"{self.nombre} con el ID {self.id} está estudiando {self.materias}"
    
    def hacer_tarea(self,materias,tarea):
        if materias in self.materias:
            self.tareas[materias]=tarea
            return f"{self.nombre} con el ID {self.id} hizo la tarea {tarea} de la materia {materias}"
        else: 
            return f"{self.nombre} con el ID {self.id} no está estudiando la materia {materias}"
    
    def entrar_clase(self,materias):
        return f"{self.nombre} con el ID {self.id} ha entrado a la clase de {materias}"
    
 #Crear instancias de la clase alumno
Alumno1 = Alumno("Dany Moran",20150,9)
Alumno2= Alumno("Mateo Gonzalez",2804,10)

#Obtener información de los alumnos
print(Alumno1.obtener_informacion())
print(Alumno2.obtener_informacion())

#Estudios
print(Alumno1.estudiar("Quimica"))
print(Alumno2.estudiar("Matematicas"))

#Aplicar metodos
print(Alumno1.entrar_clase("Quimica"))
print(Alumno1.hacer_tarea("Quimica","Tarea 1"))
print(Alumno2.hacer_tarea("Quimica","Tarea 2"))
