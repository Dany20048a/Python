class persona:
    def __init__ (self, nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.__contraseña="1234"

    def especializacion(self): #metodo sin implementacion
        pass

    def usuario(self): #publico
        return self._usuario

    def _correo(self): #privado
        return self.correo
    
    def comprobacion(self,contraseña): #protegido
        if contraseña == self.__contraseña:
            return self.especializacion()
        else:
            return "invalida",None

    def __str__(self): #instancia de Persona al convertirla en una cadena de caracteres
        return f"{self.nombre} ({self.edad} años) sexo: {self.sexo}"
    
class trabajador(persona): #subclases
    def __init__ (self,nombre,edad,sexo,empresa,salario):
        super().__init__(nombre,edad,sexo) #atributos de persona
        self.empresa=empresa
        self.salario=salario

    def __str__(self):
        return f"{super().__str__()} trabaja en {self.empresa}, salario: {self.salario}" 

class estudiante(persona): #subclases
    def __init__(self, nombre, edad,sexo,materias,calificacion):
        super().__init__(nombre, edad,sexo) 
        self.materias=materias
        self.calificacion=calificacion

    def __str__(self):
        return f"{super().__str__()} cursa: {self.materias}, calificacion: {self.calificacion}"

class ingeniero(trabajador):
    def especializacion(self):
        return "ingenier@" 
    
    def correo(self):
        return "ingeniero@gmail.com"
    
    def _usuario(self):
        return "inge1"
    
class informatico(trabajador):
    def especializacion(self):
        return "informatic@"
    
    def correo(self):
        return "informatico@gmail.com"
    
    def _usuario(self):
        return "info1"
    
class universitario(estudiante):
    def especializacion(self):
        return "estudiante"
    
    def correo(self):
        return "estudianteUni@gmail.com"
    
    def _usuario(self):
        return "uni1"
     
class prepa(estudiante):
    def especializacion(self):
        return "estudiante"
    
    def correo(self):
        return "estudiantePrepa@gmail.com"
    
    def _usuario(self):
        return "prepa1"
    
def main():
    Ingeniero = ingeniero("Juan",25,"Masculino","INEGI",420000)
    Informatico =informatico("Ruby",28,"Femenino","Softtek",25000)
    Universitario= universitario("Pepe",22,"Masculino",["Quimica","Matematicas"],10)
    Prepa=prepa("Sofia",16,"Femenino",["Español","Historia"],8)

    #Herencia (crear clases hijos que heredan atributos y metodos del padre)
    contraseña_in=input("Ingrese la contraseña: ")
    espe=Ingeniero.comprobacion(contraseña_in)
    espe2=Prepa.comprobacion(contraseña_in)

    print(f"{Ingeniero.nombre} correo: {Ingeniero.correo()} usuario: {Ingeniero._usuario()} especializacion: {espe}")
    #print(f"{Informatico.usuario()}")
    print(f"{Prepa.nombre} correo: {Prepa.correo()} usuario: {Prepa._usuario()} especializacion: {espe2}")
    
    #polimorfismo (reiterpretar los metodos de los hijos para el padre, es decir, tomar como prioridad al hijo)
    personas = [Ingeniero,Informatico,Universitario,Prepa]
    for person in personas:
        print (f"{person} es: {person.especializacion()}") 

main()
