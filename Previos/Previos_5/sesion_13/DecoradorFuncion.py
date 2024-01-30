# Se define una función que toma a func como argumento
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)

        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide  # Es la decoración de la función  divide con la función decoradora smart_divide


def divide(a, b):
    print(a/b)


divide(2, 5)
divide(2, 0)
