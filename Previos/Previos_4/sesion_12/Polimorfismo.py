# Definicion de una clase principal

class Polygon:

    def render(self):
        print("Rendering Polygon...")

# Declaricion de clase hijas que heredan de la clase Polygon.

class Square(Polygon):
    
    def render(self):
        print("Rendering Square...")
        
class Circle(Polygon):
    
    def render(self):
        print("Rendering Circle...")
               
             
        
s1 = Square() # Instancia
s1.render()

c1 = Circle() #Instancia 
c1.render()