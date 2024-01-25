class Person:
    
    def __init__(self, name, age):
        
        # Inicializacion de los atributos privados
        self.__name = name
        self.__age = age
        

p1 = Person("John", 20) # Creacion  de la instancia de la clase Person

# Intenta acceder al atributo fuera de la clase lo que va a generar un error debido a que los atributos son privados 
p1.__name 