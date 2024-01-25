# Definicion de la clase
class Bike:
    # Se crean los atributos 
    name = " "
    gear = 0
    
bike1 = Bike()  # Se crea una instancia de la clase Bike

# Modifica los atributos de la instacia 
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")