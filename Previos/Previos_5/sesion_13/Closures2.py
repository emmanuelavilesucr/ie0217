def calculate():
    num = 1
    
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()

# Muestra el resultado de llamar a la función inner_func a través de la variable odd
print(odd())
print(odd())
print(odd())

odd2 = calculate() # Imprime el resultado de llamar a la función interna 'inner_func' a través de la variable odd2
print(odd2())


