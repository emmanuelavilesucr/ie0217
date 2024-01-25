class Person: 
    
    # Este metodo esta encargado de inicializar las propiedades de la clase
    def __init__(self, name, age):
        self.name = name
        self.age = age   
    
    # Este metodo es el encargado de mostrar la informacion de la persona
        
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")