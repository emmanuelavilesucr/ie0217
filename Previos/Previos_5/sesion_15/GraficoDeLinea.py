import matplotlib.pyplot as plt   # Se importa la libreria Matplotlib

# Se crean listas y se asignan a variables 
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

plt.plot(x, y)  # Crea un gráfico de línea utilizando los datos en las listas


# Etiqueta los ejes y agrega un titulo al grafico
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafico de Linea Simple")
plt.grid(True)   # Activa la cuadrícula en el gráfico 

plt.show()   # Muestra el grafico

