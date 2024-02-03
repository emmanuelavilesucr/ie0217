import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt   # Se importa la funcion sqrt de la biblioteca math que es utilizada para el calculo de operaciones con raices cuadradas

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3  * X + np.random.randn(100, 1)

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=42)
    
    
modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

# Se declaran variables encargadas de realizar calculos
mae = mean_squared_error(y_test, y_pred)  # Valor absoluto (Error)
mse = mean_squared_error(y_test, y_pred)  # Cuadratico (Error)
rmse = sqrt(mse)                          # Raiz cuadrada


rae = np.sum(np.abs(y_test - y_pred)) / \
    np.sum(np.abs(y_test - np.mean(y_test)))
rse = np.sum((y_test - y_pred)**2) / np.sum((y_test - np.mean(y_test))**2)

# Imprime los valores de las variables asignadas anteriormente.
# .2f se refiere a la opcion de mostrar un resultado numerico en un formato de dos decimales
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"RAE: {rae:.2f}")
print(f"RSE: {rse:.2f}")

# nEsta es la configuracion del grafico generado por matplotlib.
plt.scatter(X_test, y_test, label="Datos de prueba", color="blue")
plt.plot(X_test, y_pred, label="Predicciones", color="red")
plt.title("Regresion Lineal y Errores")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()

# La funcion de este ciclo for es iterar sobre cada prediccion.
for i in range(len(X_test)):
    plt.plot([X_test[i], X_test[i]],
             [y_test[i], y_pred[i]],
             linestyle="--", color="gray")

plt.show()
    