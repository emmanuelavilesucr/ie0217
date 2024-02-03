import numpy as np   #  La biblioteca numpy es utilizada en la operacion de con datos numericos 
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
from sklearn.pipeline import make_pipeline  # La funcion make_pipeline de la biblioteca sklearn es utrilizada para el procesamiento de datos 

# Aqui nuevamente se declaran las variables X e y, las cuales albergan numeros generados aletoriamente
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

# En esta parte se asigna el nombre del grafico, nombre de cada eje. (Grafico de la Regresion no lineal) 
plt.scatter(X, y)
plt.title("Datos de Regresion No Lineal")
plt.xlabel("X")
plt.ylabel("y")
plt.show()


grado_polinomio = 2    # Se declara una variable que alberga un dato numerico de tipo entero

# Se asigna la funcion make_pipeline a un variable encargada de crear una regresion polinomica
modelo_polinomico = make_pipeline(
    PolynomialFeatures(grado_polinomio), LinearRegression())
modelo_polinomico.fit(X, y)

# A continuacion se visualizan las regresiones polinomicas
X_test = np.linspace(0, 2, 100).reshape(100, 1)
y_pred = modelo_polinomico.predict(X_test)



plt.scatter(X, y)
plt.title(X_test, y_pred, color= "red",
          label=f"Regresion Polinomica ({grado_polinomio} grado)")

# A continuacion se establece el nombre del grafico, nombre de cada uno de los ejes y leyenda. (Grafico de la Regresion polinomica).
plt.title("Regresion Polinomica")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

