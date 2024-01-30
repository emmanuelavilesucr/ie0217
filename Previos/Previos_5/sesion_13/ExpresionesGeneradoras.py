# Se define una funcion encargada de generar la secuencia de Fibonacci 
def fibonacci_numbers(nums):
    x, y = 0, 1

    for _ in range(nums):
        x, y = y, x+y
        yield x

# Se define una funcion que genera los cuadrados de los números en la entrada.
def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))  # Muestra la suma de los cuadrados de los primeros diez terminos

