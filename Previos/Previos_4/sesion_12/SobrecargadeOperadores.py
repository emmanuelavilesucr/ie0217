class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y
        
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    
    def __add__(self, other):
        
         # Se realiza la sobrecarga del operador de suma para Point
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2) # Imprime la suma
