c = 1 # Se define una variable de tipo entero 

def add():
    
    global c # Indica que c es global dentro de la funcion
    
    c = c + 2   # Se realiza una operacion sobre la variable c y el resultado se alberga sobre una nueva variable
    print(c)
    
add() # Se llama a la funcion
    

