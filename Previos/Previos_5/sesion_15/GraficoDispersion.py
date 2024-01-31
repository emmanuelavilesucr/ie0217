import matplotlib.pyplot as plt   # Se importa la libreria Matplotlib
 
# Se crean listas y se asignan a variables 
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

plt.scatter(x, y, label="Puntos")


# Etiqueta los ejes y agrega un titulo al grafico
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafico de Dispersion")
plt.legend()    # Muestra la leyenda 

plt.show()   # Muestra el grafico


