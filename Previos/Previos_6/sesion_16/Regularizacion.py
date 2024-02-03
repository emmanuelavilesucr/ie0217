import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline 

# Se establecen las variables X e y
# Tambien se asigna la creacion de datos aleatorios para las variables
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 8.5 * X**2 + X + 2 + np.random.randn(100, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
     
# En esta parte se crean los modelos de regrasion
modelo_polinomico = make_pipeline(
    PolynomialFeatures(degree=2), LinearRegression())
modelo_polinomico.fit(X_train, y_train)

# Lasso (Pipeline)
modelo_lasso = make_pipeline(PolynomialFeatures(degree=2), Lasso(alpha=0.1))
modelo_lasso.fit(X_train, y_train)

# Ridge (Pipeline)
modelo_ridge = make_pipeline(PolynomialFeatures(degree=2), Ridge(alpha=0.1))
modelo_ridge.fit(X_train, y_train)


# Se asignan los datos que seran utilizados para visualizacion
X_test_sorted, y_pred_polinomico_sorted = \
    zip(*sorted(zip(X_test, modelo_polinomico.predict(X_test))))

X_test_sorted, y_pred_lasso_sorted = \
    zip(*sorted(zip(X_test, modelo_lasso.predict(X_test))))

X_test_sorted, y_pred_ridge_sorted = \
    zip(*sorted(zip(X_test, modelo_ridge.predict(X_test))))

# En esta parte se establece las configuraciones del grafico generado por matplotlib
plt.scatter(X_test, y_test, label="Datos de prueba", color="blue")
plt.plot(X_test_sorted, y_pred_polinomico_sorted, label="Regresion Polinomica", 
         color="green")
plt.plot(X_test_sorted, y_pred_lasso_sorted, label="Lasso (L1)", color="red")
plt.plot(X_test_sorted, y_pred_ridge_sorted, label="Ridge (L2)", 
         color="orange")
plt.title("Comparacion de Modelos con Regularizacion")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()