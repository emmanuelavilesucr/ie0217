import requests

users_response = requests.get("https://jsonplaceholder.tyicode.com/users")
users_data = users_response.json()

posts_response = requests.get("https://jsonplaceholder.tyicode.com/post")
posts_data = posts_response.json() # Para el contenido JSON


user_posts = {} # Se crea un diccionario vacio encargado de almacenar los post

# Por medio del ciclo for inicia el diccionario 
for user in users_data:
    user_posts[user["id"]] = []  # Se crea una lista vacia
    
# Realiza una operacion de distribucion de los post    
for post in posts_data:
    user_id = post.get("userId")
    if user_id in user_posts:
        user_posts[user_id].append({
            "title": post["title"],
            "body": post["body"]
        }) 
        
for user_id, posts in user_posts.items():
    user = next((user for user in users_data if user["id"] == user_id), None)  # Se establece una variable de busqueda por medio de Id de usuario
    
    if user:
        print(f"\nPublicaciones de {user["name"]} ({user["email"]}):\n")  # Muestra los post 
        for post in posts:
            print(f"Title: {post["title"]}\nBody: {post["body"]}\n") # Muestra el titulo de cada post
            
    else:
        print(f"No se encontraron datos para el usuario con ID {user_id}")
