class Animal:
    name = "" # Atributo del nombre del animal 
    
    # Metodo 
    def eat(self):
        print("I can eat")
        
# Se define la clase Dog que hereda de la clase Animal        
class Dog(Animal):
    
    # Metodo
    def display(self):
        print("My name is ", self.name)
        
   
labrador = Dog() # creacion de la instancia

labrador.name = "Rohu"  # Asignacion de un nombre al atributo name 
labrador.eat() # Llama al metodo de la clase Animal
labrador.display() # Llama al metodo de la clase Dog