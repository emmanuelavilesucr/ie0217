import matplotlib.pyplot as plt   # Se importa la libreria Matplotlib

categorias = ["A", "B", "C", "D"] # S

# Se crean listas y se asignan a variables 
valores = [15, 8, 12, 10]
tendencia = [5, 10, 8, 13]


fig, axs = plt.subplots(1, 2, figsize=(10, 4))   # Crea una figuras, ejes, filas y columnas

# En el primer grafico se trazan las barras con las categorías y valores 
axs[0].bar(categorias, valores, color="royalblue")
axs[0].set_title("Grafico de Barras")  # Asigna el nombre

# En el segundo grafico se trazan las categorías y tendencia 
axs[1].plot(categorias, tendencia, color="green", marke= "o")
axs[1].set_title("Grafico de Linea")  # Asigna el nombre 

# Itera sobre ambos graficos y establece etiquetas para los ejes
for ax in axs:
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Valores")


plt.tight_layout()   # Ajusta la disposicion de los elementos en la figura
plt.show()   # Muestra el grafico


