# Definicion de la primera clase base

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")
        
# Definicion de una segunda clase base

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")
  
# Definicion de una clase derivada, que hereda de SuperClass1 y SuperClass2
      
class Derived(SuperClass1, SuperClass2):
    pass


d1 = Derived() # instancia
d1.info()  
