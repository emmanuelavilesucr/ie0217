def my_generator(n):

    value = 0 # Inicializa una variable con el valor 0

    # Se ejecuta el bucle while mientras que value sea menor que n
    while value < n:

        yield value

        value += 1

# itera sobre los valores generado con n igual a 3
for value in my_generator(3):
    print(value)
