message = "Hello" # Se asigna una cadena de letras a la variable message

# Se declara la funcion greet

def greet():
    
    message = "Hello"
    print("Local", message)
    
greet()    # Se llama a la funcion 
print("Global", message) # imprime global + la variable message