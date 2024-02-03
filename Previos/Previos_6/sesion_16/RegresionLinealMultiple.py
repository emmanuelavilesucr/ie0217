import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import make_regression

# Se generan los datos del codigo 
X, y = make_regression(n_samples=100, n_features=3, noise=20, random_state=42)

# Se establece un DataFrame para el almacenamiento de datos par tener mayor claridad
df = pd.DataFrame(X, columns=["Tamano", "Habitaciones", "Distancia_Ciudad"])
df["Precio"] = y 

#  Se dividen los datos en conjunto de entrenamiento
X_train, X_test, y_train, y_test = train_test_split( 
    df[["Tamano", "Habitaciones", "Distancia_Ciudad"]],
    df["Precio"], test_size=0.2, random_state=42)

# Se crea y ajusta el modelo de la regresion lineal multiple
modelo = LinearRegression()  # Se crea un instacion de la funcion Regresion Lineal
modelo.fit(X_train, y_train)

# Le muestra un mensaje a usuario con los Coeficientes e intercepciones de los datos
print("Coeficiente:", modelo.coef_)
print("Intercepcion:", modelo.intercept_)

y_pred = modelo.predict(X_test)    # En est linea se establecen las prdicciones del conjunto
fig = plt.figure(figsize=(12, 6))  # Se crea una variable a la que se le asigna la visualizacion  de la regresion lineal multiple

# Se crea la configuracion del Grafico 1. (Tamano vs. Precio).
ax1 = fig.add_subplot(131, projection="3d")
ax1.scatter(
    X_test["Tamano"], X_test["Habitaciones"],
    y_test, c="blue", marker="o", alpha=0.5)
ax1.set_xlabel("Tamano")
ax1.set_ylabel("Habitaciones")
ax1.set_zlabel("Precio Verdadero")
ax1.set_title("Precio Verdadero vs. Tamano y Habitaciones")

# Se crea la configuracion del Grafico 2. (Tamano vs. Precio Predicho).
ax2 = fig.add_subplot(132, projection="3d")
ax2.scatter(
    X_test["Tamano"], X_test["Habitaciones"],
    y_pred, c="red", marker="o", alpha=0.5)
ax2.set_xlabel("Tamano")
ax2.set_ylabel("Habitaciones")
ax2.set_zlabel("Precio Predicho")
ax2.set_title("Precio Predicho vs. Tamano y Habitaciones")

# Se crea la configuracion del Grafico 3. (Comparacion de Precio Verdadero y Precio Predicho).
ax3 = fig.add_subplot(133)
ax3.scatter(y_test, y_pred, c="green", alpha=0.5)
ax3.plot(
    [min(y_test), max(y_pred)], [min(y_test), max(y_test)],
    linestyle="--", color="red", linewidth=2)
ax3.set_xlabel("Precio Verdadero")
ax3.set_ylabel("Precio Predicho")
ax3.set_title("Comparacion de Precio Verdadero y Precio Predicho")

plt.tight_layout()
plt.show()