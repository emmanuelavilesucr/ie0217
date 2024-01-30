# Se declara la funcion add que toma dos parámetros y realiza una suma
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x,  y)

result = calculate(add, 4, 6)   # Llama a la funcion add y proporciona los numeros para realizar la suma 
print(result)

