# Se define la función encargada de agregar asteriscos alrededor de la función
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner
   

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
        
    return inner

# D=Se establece la decoración de las funciones
@star
@percent

def printer(msg):
    print(msg)

printer("Hello")
