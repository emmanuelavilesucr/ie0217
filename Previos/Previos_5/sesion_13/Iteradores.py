my_list = [4, 7, 0]  # Se define una lista 

iterator = iter(my_list)   # Se crea un iterador a partir de la lista

# Imprime los elementos del iterador
print(next(iterator))
print(next(iterator))
print(next(iterator))


for element in my_list:
    print(element)
