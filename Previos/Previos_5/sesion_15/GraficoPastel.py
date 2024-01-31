import matplotlib.pyplot as plt  # Se importa la libreria Matplotlib

proporciones = [30, 20, 25, 15]
etiquetas = ["A", "B", "C", "D"]

plt.pie(proporciones, labels=etiquetas, autopct="%1.1%", startangle=140, 
        colors=["gold", "lightcoral", "lightgreen", "lightskyblue"])

# Se agrega un titulo al grafico
plt.title("Grafico de Pastel")

plt.show()   # Muestra el grafico