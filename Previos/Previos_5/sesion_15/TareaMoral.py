# Se importan las librerias 
import matplotlib.pyplot as ptl
import numpy as np

categorias = ["A", "B", "C", "D"]
valores1 = [15, 8, 12, 10]
valores2 = [12, 10, 15, 7]
tendencia = [11, 9, 13, 9]

fig, ax = ptl.subplots()   # Se crean la figura y ejes del grafico

ancho_barra = 0.35
indice = np.arange(len(categorias))

# Se crean las barras para las dos series
bar1 = ax.bar(indice - ancho_barra / 2, valores1, ancho_barra, label= "Serie 1", color="royalblue")
bar2 = ax.bar(indice + ancho_barra / 2, valores2, ancho_barra, label= "Serie 2", color="ligthcoral")

ax.plot(indice, tendencia, label="Tendencia", marker="o", color="green")   # Traza la línea de tendencia con marcadores verdes

# Esta parte es la configuracion de etiquetas del grafico
ax.set_xlabel("Categorias")
ax.set_ylabel("Valores")
ax.set_title("Grafico de Barras Agrupadas con Tendencia")
ax.set_xticks(indice)
ax.set_xticklabels(categorias)
ax.legend()

# Se agregan etiquetas de valores sobre las barras
for bar in [bar1, bar2]:
    for rect in bar:
        height = rect.get_height()
        ax.annotate("{}".format(height),
                xy=(rect.ger_x() + rect.get_width / 2, height),
                xytex =(0, 3),
                textcoords="offset points",
                ha="center", va="bottom")


ptl.grid(axis="y", linestyle="--", alpha=0.7)    # Activa la cuadrícula en el gráfico 
ptl.tight_layout()  # Ajusta la disposicion de los elementos en la figura
ptl.show()  # Muestra el grafico

