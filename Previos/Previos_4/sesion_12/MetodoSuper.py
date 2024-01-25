class Animal:
    name = ""  
    
    def eat(self):
        print("I can eat")
           
class Dog(Animal):
    
    def eat(self):
        
        super().eat()   # Llamada al metodo eat de la clase Animal mediante super()
        print("I like to eat bones")
        
   
   
labrador = Dog() 
labrador.eat() 
