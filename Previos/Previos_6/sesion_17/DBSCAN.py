import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN  # Se llama a la funcion DBSCAN, la cual es un algoritmo relacionado con el clustering no lineal


X, _ = make_moons(n_samples=200, noise=0.05, random_state=42)  # Generacion de los datos para el grafico

# A continuacion, se realiza la configuracion del DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

# Esta es la parte relacionada con la generacion del grafico de matplotlib
plt.scatter(
    X[:, 0], X[:, 1], c=dbscan_labels, cmap="viridis", edgecolor="k", s=50 )  # Se ajusta y establece formato del grafico
plt.title("Resultado del Clustering DBSCAN")  # Se elige el nombre del grafico
plt.xlabel("Caracteristica 1")  # Se le pone una etiqueta al eje horizontal
plt.ylabel("Caracteristica 2")  # Se establece el nombre del eje vertical
plt.show()  # Muestra el grafico al ususario 
