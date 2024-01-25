def find_sum(*numbers):
    result = 0
    
    # Itera sobre los numeros proporcionados como argumentos
    for num in numbers:
        result = result + num
    
    # Imprime la suma de los numeros
    print("Sum = ", result)
    
find_sum(1, 2, 3)
find_sum(4, 9)