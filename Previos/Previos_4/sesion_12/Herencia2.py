class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


# Se crea la clase Triangule que hereda de Polygon

class Triangle(Polygon):
    def __init__(self): 
        Polygon.__init__(self,3)   # Llama al constructor de la clase base con 3 lados para un triángulo
    
    def findArea(self):
        a, b, c = self.sides
        
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of the triangule is %0.2f" %area)
       
        
t = Triangle() # creacion de la instancia 

# Llama a los metodos de las clase
t.inputSides()
t.dispSides()
t.findArea()