import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score


# En esta seccion se establecen las variables X e y.
# Se generan datos aleatorios utilizando random para las variables X e y. 
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3  * X + np.random.randn(100, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
    
modelo = LinearRegression()  # Se asigna la funcion de Regresion Lineal a una variable
modelo.fit(X_train, y_train) # En esta linea se realiza un especie de ajuste para realizar predicciones de los valores X_train e y_train.
y_pred = modelo.predict(X_test)  # Se establece una varaible  encargada de realizar predicciones del valor X_test
r2 = r2_score(y_test, y_pred) # Se declara una variable encargada de albergar los valores de y_test e y_pred
                              # Por otro lado, r2_score toma los dos valores de la variable y realiza una operacion para extraer el coeficiente

# Seccion del codigo encargada de la generacion del grafico por medio de la biblioteca matplotlib
plt.scatter(X_test, y_test, label="Datos de prueba", color="blue")
plt.plot(X_test, y_pred, label=f"Regresion Lineal (R^2={r2:.2f})", 
         color="red")
plt.title("Regresion Lineal y Coeficiente de Determinacion R^2")  # Se define el nombre del grafico
plt.xlabel("X") # Se establece el nombre del eje horizontal 
plt.ylabel("y") # Se establece el nombre del eje vertical
plt.legend()
plt.show()  # Finalmente, muestra el grafico al usuario 