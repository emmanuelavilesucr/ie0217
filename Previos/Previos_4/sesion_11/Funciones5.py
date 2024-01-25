# En esta funcion se emplea el uso de argumentos
def add_numbers(a = 7, b = 8):
    sum = a + b
    print("Sum", sum)

# Llama a la funcion con diferentes configuraciones de argumentos
add_numbers(2, 3)
add_numbers(a = 2)
add_numbers()
