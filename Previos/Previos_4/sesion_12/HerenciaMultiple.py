class Mammal:
    def mammal(self):
        print("Mammals can give direct birth.")
        
class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap. ")
        
        
# Se crea la clase Bat que hereda de la clase Mammal y WingedAnimal
     
class Bat(Mammal, WingedAnimal):
    pass

b1 = Bat() # Creacion de una instancia

# Llamada de los metodos
b1.mammal()
b1.winged_animal_info()
