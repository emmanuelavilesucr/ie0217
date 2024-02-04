from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# En esta parte se crea una variable que almacena un dato random
np.random.seed(42)
X = np.random.rand(100, 2) * 10


inertias = []  # Se crea una lista llamada inertias 

# Este ciclo for itera sobre los posibles valores de k
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42) # Ajuste de KMeans
    kmeans.fit(X)   # Ajuste de KMeans
    inertias.append(kmeans.inertia_)
    
# Se establece la configuracion del grafico.
plt.plot(range(1, 11), inertias, marker="o")
plt.title("Metodo del Codo")
plt.xlabel("Numero de Clusters (k)")
plt.ylabel("Inercia")
plt.show()
