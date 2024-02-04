from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Se establece la variable X y se le asigna un dato aletorio 
np.random.seed(42)
X = np.random.rand(100, 2) * 10

# Grafico 1.(Puntos de los datos aleatorios).
plt.figure(figsize=(12, 5)) # Aqui se define el tamano del grafico 
plt.subplot(1, 2, 1)   # Se establece el numero de filas y columnas  
plt.scatter(X[:, 0], X[:, 1], c="blue", marker="o")  # Se establecen la dispersion de los datos y se establece el color y forma de los marcadores
plt.title("Puntos de Datos Aleatorio")  # Se declara el nombre del grafico 
plt.xlabel("Caracteristica 1") # Se asigna el nombre del eje horizontal
plt.ylabel("Caracteristica 2") # Se asigna el nombre del eje vertical

# Se hacen los ajustes relacionados con uso de KMeans y los clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

labels = kmeans.labels_    # Etiquetas de los clusters
centroids = kmeans.cluster_centers_ # Coordenadas de los centroids


# Se establece la configuracion del segundo grafico. (Resultado del clustering con KMeans)
plt.subplot(1, 2, 2)
for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1],
                c=("r" if labels[i] == 0 else "b" if labels[i] == 1 else "g"),
                marker="o")
    
    
plt.scatter(centroids[:, 0], centroids[:, 1], c="black", marker="X", s=200,
            label="Centroids")
plt.title("Resultado del clustering con K-Means")
plt.xlabel("Caracteristica 1")
plt.ylabel("Caracteristica 2")
plt.legend()
plt.tight_layout()
plt.show()
