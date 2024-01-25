from math import pi

# Se define una clase principal 

class Shape:
    def __int__(self, name):
        self.name = name
        
    def area(self):
        pass
    
    def fact(self):
        return "I am a two-dimensional shape."
    
    def __str__(self):
        return self.name
    

# Se define una clase que hereda de la clase Shape 

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square") # Llamada al metodo init mediante super()
        self.length = length
        
    def area(self):
        return self.lengrh**2
    
    def fact(self):
        return "Squares have each angle equal to 90 degrees"
    
    
# Se define otra clase que hereda de la clase Shape  

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle") # Llamada al metodo init mediante super()
        self.radius = radius
    
    def area(self):
        return pi*self.radius**2 
 
# Creacion de las instancias
   
a = Square(4)
b = Circle(7)

# Realiza impresion de los metodos

print(b)
print(b.fact())
print(a.fact())
print(b.area())