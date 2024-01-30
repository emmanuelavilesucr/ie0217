def make_pretty(func):
    # Se define una funcion interna
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty  # Decoracion de la funcion

# Se define una nueva funcion 
def ordinary():
    print("I am ordinary")

ordinary() # Se llama a la funcion
