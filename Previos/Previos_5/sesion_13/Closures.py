def greet(name):
    
    # Se define una funcion interna
    def display_name():
        print("Hi", name)

    display_name()  # Llama a la función interna para mostrar el saludo

greet("John")


def greet():
    
    # La función lambda toma la variable del entorno externo y retorna un saludo
    name = "John"
    return lambda: "Hi " + name

message = greet()
print(message())
