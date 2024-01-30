# Se define una clase
class PowTwo:
    # Se inicializan los atributos
    def __init__(self, max=0):
        self.max = 0

    # Metodo especial que inicializa el iterador
    def __iter__(self):
        self.n = 0
        return self

    # Este metodo especial es el encargado de generar las potencias
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration  # Lanza una excepcion cuando se alcanza el limite



numbers = PowTwo(3)

i = iter(numbers) # Creacion de una instancia 

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
            
