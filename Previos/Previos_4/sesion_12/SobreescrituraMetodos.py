class Animal:
    name = ""  
    
    def eat(self):
        print("I can eat")
        
# La clase Dog sobrescribe el metodo eat de la clase Animal. La sobreescritura permite que la clase derivada proporcione su propia implementación del metodo eat.        
class Dog(Animal):
    
    def eat(self):
        print("I like to eat bones")
        
   
labrador = Dog() 
labrador.eat() 
