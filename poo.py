class Animal: 
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def hacer_sonido(self):
        pass

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
    
class Mascota(Animal):
    def __init__(self,nombre,edad,tipo_pelo):
        super().__init__(nombre,edad)
        self.tipo_pelo=tipo_pelo

class Perro(Mascota):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Mascota):
    def hacer_sonido(self):
        return "Miau"
    
class Vaca(Mascota): #polimorfismo (mascota)
    def hacer_sonido(self):
        return "Muu"
    
def main():
#Metodos que comparten las caracterisitcas
#sobre carga repetir metodos que ya existe pero hacerlo de una forma distinita, (metodos funcionales)
    perro =Perro ("Firulais",3,"corto")
    gato = Gato ("Bigotes",2,"Largo")
    vaca = Vaca("Gris",4,"Corto")

#Herencia
    print(f"{perro.nombre} tiene pelo {perro.tipo_pelo}")
    print(f"{gato.nombre} tiene pelo {gato.tipo_pelo}")

#polimorfismo
    animales = [perro,gato,vaca]
    for animal in animales: 
        print(f"{animal} hace: {animal.hacer_sonido()}")

#sobrecarga de métodos
    def hacer_sonido_personalizado(animal):
        print(f"{animal} dice: {animal.hacer_sonido()}")

    hacer_sonido_personalizado(perro)
    hacer_sonido_personalizado(gato)
    hacer_sonido_personalizado(vaca)

if __name__ == "__main__":
    main()