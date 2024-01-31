import matplotlib.pyplot as plt  # Se importa la libreria Matplotlib

# Se crean listas y se asignan a variables 
datos = [15, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]


plt.boxplot(datos)  # Crea el diagrama de caja utilizando los la variable datos

# Etiqueta los ejes y agrega un titulo al grafico
plt.ylabel("Valores")
plt.title("Grafico de Caja")

plt.show()   # Muestra el grafico


