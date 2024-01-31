import matplotlib.pyplot as plt   # Se importa la libreria Matplotlib

# Se crean los datos para los ejes
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

plt.plot(x, y, label="Datos de ejemplos")   # Se crea un grafico de linea con los datos 

plt.annotate("Valor Maximo", xy=(5, 14), xytext=(3, 16), arrowprops=dict(facecolor="black", shrink=0.05),)    # Agrega una anotación en un punto hacia otro punto 

# Etiqueta los ejes y agrega un titulo al grafico
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafico con Anotacion")
plt.legend() # Muestra la leyenda 

plt.show()   # Muestra el grafico


