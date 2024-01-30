# Abre el archivo en modo lectura
with open("test.txt", "r") as file1:
    read_content = file1.read()  # Lee el contenido del archivo y asigna el contenido a una variable 
    print(read_content)
