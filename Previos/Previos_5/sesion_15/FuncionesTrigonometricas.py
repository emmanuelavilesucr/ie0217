import matplotlib.pyplot as plt  # Se importa la libreria Matplotlib
import numpy as np   # Se importa la librería NumPy

x = np.linspace(0, 2 * np.pi, 100)  
y1 = np.sin(x)  # Calcula sin en cada punto x
y2 = np.cos(x)  # Calcula coseno en cada punto x


plt.plot(x, y1, label="Seno")   # Crea un gráfico de línea de la funcion Seno
plt.plot(x, y2, label="Coseno")  # Crea un gráfico de línea de la funcion Coseno
 

# Etiqueta los ejes y agrega un titulo al grafico
plt.xlabel("Angulo (rad)")
plt.ylabel("Valor")
plt.title("Funciones Seno y Coseno")
plt.legend()  # Muestra la leyenda 


plt.show()   # Muestra el grafico
