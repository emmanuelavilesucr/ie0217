import matplotlib.pyplot as plt # Se importa la libreria Matplotlib

categorias = ["A", "B", "C", "D"]
valores = [15, 8, 12, 10]

plt.bar(categorias, valores, color="royalblue", edgecolor="black")  # Crea el gráfico de barras utilizando las categorías y valores


# Etiqueta los ejes y agrega un titulo al grafico
plt.xlabel("Categorias", fontsize=12)
plt.ylabel("Valores", fontsize=12)
plt.title("Grafico de Barras", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Activa la cuadrícula en el gráfico 


for i, v in enumerate(valores):

    plt.text(i, v + 0.5, str(v), ha= "center", va= "bottom", fontsize=10)

plt.show()   # Muestra el grafico
