import matplotlib.pyplot as plt  # Se importa la libreria Matplotlib

categorias = ["A", "B", "C", "D"]
valores = [15, 8, 12, 10]

plt.bar(categorias, valores, color="royalblue")  # Crea el gráfico de barras


# Etiqueta los ejes y agrega un titulo al grafico
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Grafico de Barras Verticales")

plt.show()   # Muestra el grafico


