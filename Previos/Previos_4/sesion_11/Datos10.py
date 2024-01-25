squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in squares)
print(2 not in squares)   # Verifica si la clave 2 no esta en el diccionario
print(49 in squares)    # Verifica si el valor 49 esta en los valores del diccionario

# Itera sobre el diccionario
for i in squares:
    print(squares[i])