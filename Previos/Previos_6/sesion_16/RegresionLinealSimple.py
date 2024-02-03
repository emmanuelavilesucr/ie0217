import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Se declaran las variables X e y, encargadas de albergar datos generados de forma aleatorio por medio de la funcion random
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1) 


modelo = LinearRegression() # Se una instancia a la que se asigna la funcion de Regresion Lineal
modelo.fit(X, y) # Realiza un ajuste de los datos X e y 

# Por medio de mensaje le muestra al usuario el coeficiente y la interception de las variables X e y
print("Coeficiente:", modelo.coef_[0][0])
print("Intercepcion:", modelo.intercept_[0])


# En esta seccion del codigo se genera un grafico de la Regresion Lineal utilizando la biblioteca matplotlib. 
plt.scatter(X, y)
plt.plot(X, modelo.predict(X), color="red", linewidth=3)
plt.title("Regresion Lineal") # Titulo del grafico 
plt.xlabel("X") # Nombre del eje horizontal  
plt.ylabel("Y") # Nombre del eje vertical 
plt.show()  # Muetra grafico al usuario 