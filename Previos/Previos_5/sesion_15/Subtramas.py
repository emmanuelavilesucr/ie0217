import matplotlib.pyplot as plt

# Se crean listas y se asignan a variables 
x = [1, 2, 3, 4, 5]
y1 = [10, 12, 5, 8, 14]
y2 = [5, 8, 9, 6, 10]

fig, axs = plt.subplots(1, 2)  # Crean ejes, filas y columnas

# En el primer se establecen los datos
axs[0].plot(x, y1, label="Serie A")
axs[0].set_title("Subtrama 1")  # Asigna el nombre

# En el segundo grafico se establecen los datos
axs[1].plot(x, y2, label="Serie B", color="red")
axs[1].set_title("Subtrama 2") # Asigna el nombre

# Itera sobre ambos graficos y establece etiquetas para los ejes
for ax in axs:
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()


plt.tight_layout()   # Ajusta la disposicion de los elementos en la figura

plt.show() # Muestra el grafico


