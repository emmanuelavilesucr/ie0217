import requests # Esta biblioteca es utilizada para hacer solicitudes de HTTP

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")  # Realiza la solicitud de HTTP
print("Tipo:", type(response)) # Muestra el tipo de dato de response
print("Respuesta:", response)  # Imprime la respuesta
print("Respuesta text:", response.text)  # Muestra la respuesta pero esta vez lo hace el formato de texto

print("Respuesta:", response.__dict__) # Muestra la respuesta mediante __dict__
                                       # la funcion de __dict__ es almacenar atributos 