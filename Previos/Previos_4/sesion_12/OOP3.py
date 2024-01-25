class Room:
    # Atributos
    length = 0.0
    breadth = 0.0
    
    # Se implementa un metodo encargado de calcular el area de la habitacion 
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)
       
# Se crea una instancia  
study_room = Room()

# Se asignan valores a los atributos de la instancia
study_room.length = 42.5
study_room.breadth = 30.8 

study_room.calculate_area() # Llama al metodo encargado del calculo del area de la habitacion 

