def greeting(name):
    def hello():
        return  "Hello, " + name + "!"  # Retorna un el saludo utilizando el parámetro name
    return hello  # Retorna hello como resultado de la función

greet = greeting("Atlantis")  # Llama a la función con el argumento Atlantis y se le asigna greet
print(greet())
