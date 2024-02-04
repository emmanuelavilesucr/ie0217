import requests


url = "https://www.google.com"  # Se asigna el link a la variable url
response = requests.get(url)

print("Respuesta text:", response.text)

payload = {"clave1": "valor1", "clave2": "valor2"}  # Se crea un diccionario 
response = requests.get("https://ejemplo.com/ruta", params=payload)
print(response.text)

# En esta parte se realiza la solicitud HTTP
payload = {"usuario": "juan", "contrasena": "secreta"}
response = requests.get("https://ejemplo.com/login", data=payload) # Se utiliza el parametro data para enviar los datos del diccionario al HTTP
print(response.text)

#  Se vuelven a realizar la solicitud HTTP
payload = {"usuario": "juan", "contrasena": "secreta"}
response = requests.get("https://ejemplo.com/login", json=payload)
print(response.text)

# Se realiza una solicitud
response = requests.get("https://jsonplaceholder.tyicode.com/todos/1")
print(response.status_code)
print(response.headers)   # Se imprime el encabezado del HTTP
print(response.json())   # Interpreta el contenido JSON

# A continuacion se establece un ejemplo de HTTPS empleando el uso de excepciones.
try:
    response = requests.get("https://ejemplo.com/pagina-inexistente")
    response.raise_for_status()  # Revisa si la solicitud se creo de manera correcta
    print(response.text)
    
# Si no se pudo enviar la solicitud HTTP anterior se muestra un mensaje de error 
except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")