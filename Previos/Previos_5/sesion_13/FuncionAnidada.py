def outer(x):
    def inner(y):
        return x + y   # Retorna una suma entre variables
    return inner    # Retorna la función interna inner como resultado de la función outer

add_five = outer(5)    # Llama a la función con el argumento 5 y guarda el resultado en una nueva variable 
result = add_five(6)
print(result) 


