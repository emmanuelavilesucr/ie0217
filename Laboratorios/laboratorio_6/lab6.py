import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import requests
import os

# -----------
#     1
# -----------

response = requests.get("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")

if not os.path.exists("data"):
    os.mkdir("data")
archivo = open("data/dataset.csv", "w")
archivo.write(response.text)

data = pd.read_csv("data/dataset.csv")

# Mediante X_simple e y_simple se estraen los datos relacionados a la cambio de la categoria
# Los valores de -1 y 1 de .reshape con el fin de dimensionar los datos. (De array pasa a un array de arrays)
# x = [1, 2, 3, 4, 5] -> [[1], [2], [3], [4], [5]]
# posee compatibilidad con el train_test_split 
# interprete detecta el tamano del array automaticamente por train_test_slit
X_simple = data['median_income'].values.reshape(-1, 1)  # Datos de la categoria de la categoria median_ income en el eje X\
    
y_simple = data['median_house_value'].values # Datos de la categoria median_house_value del eje y

# Esta linea se utiliza para el entrenamiento en lo ejes x e y. 20% Prueba y 80% Entrenamiento 
# Semilla random de 42
X_train, X_test, y_train, y_test = train_test_split(X_simple, y_simple, test_size=0.2, random_state=42)


model_simple = LinearRegression()  # Objeto de tipo linear

model_simple.fit(X_train, y_train) # Se realizan las predicciones 

# Se  predicen los valores del eje y. La funcion predict() toma como argumento
# Un conjunto de datos de prueba (X_test) y devuelve los valores  predichos (y_prend_simple). 
y_pred_simple = model_simple.predict(X_test)

# Se obtiene el mse de la prediccion con respecto a los datos de pruebas 
mse_simple = mean_squared_error(y_test, y_pred_simple)
print(f"Error cuadrático medio (MSE) en regresión lineal simple: {mse_simple}")



# -----------
#     2
# -----------

X_multiple = data[['median_income', 'housing_median_age', 'population']]
y_multiple = data['median_house_value'].values


X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X_multiple, y_multiple, test_size=0.2, random_state=42)


model_multiple = LinearRegression()
model_multiple.fit(X_train_multi, y_train_multi)


y_pred_multiple = model_multiple.predict(X_test_multi)


mse_multiple = mean_squared_error(y_test_multi, y_pred_multiple)
print(f"Error cuadrático medio (MSE) en regresión lineal múltiple: {mse_multiple}")

# -----------
#     3
# -----------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


X_nonlinear = data['housing_median_age'].values.reshape(-1, 1)
y_nonlinear = data['median_house_value'].values


X_train_nonlinear, X_test_nonlinear, y_train_nonlinear, y_test_nonlinear = train_test_split(X_nonlinear, y_nonlinear, test_size=0.2, random_state=42)


degree = 2
model_nonlinear = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_nonlinear.fit(X_train_nonlinear, y_train_nonlinear)


y_pred_nonlinear = model_nonlinear.predict(X_test_nonlinear)


mse_nonlinear = mean_squared_error(y_test_nonlinear, y_pred_nonlinear)
print(f"Error cuadrático medio (MSE) en regresión no lineal: {mse_nonlinear}")

# -----------
#     4
# -----------
from sklearn.linear_model import Ridge, Lasso


model_ridge = Ridge(alpha=1.0)
model_ridge.fit(X_train_multi, y_train_multi)


model_lasso = Lasso(alpha=1.0)
model_lasso.fit(X_train_multi, y_train_multi)

# -----------
#     5
# -----------
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt


X_cluster = data[['longitude', 'latitude']]


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data['cluster_kmeans'] = kmeans.fit_predict(X_cluster)


dbscan = DBSCAN(eps=0.5, min_samples=5)
data['cluster_dbscan'] = dbscan.fit_predict(X_cluster)


plt.scatter(data['longitude'], data['latitude'], c=data['cluster_kmeans'], cmap='viridis', marker='.')
plt.title('Clusters usando K-means')
plt.show()

plt.scatter(data['longitude'], data['latitude'], c=data['cluster_dbscan'], cmap='viridis', marker='.')
plt.title('Clusters usando DBSCAN')
plt.show()