import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering # Funcion utilizada para el clustering de forma jerarquica

X, y = make_blobs(n_samples=50, centers=3, random_state=42, cluster_std=1.0) # Se establecen las variables y se generan los datos 
Z = linkage(X, method="complete")   # Se configura el clustering jerarquico

# Se realiza la configuracion del grafico dendrograma
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Dendrograma Hierarchical Clustering")
plt.xlabel("Indice del Punto de Datos")
plt.ylabel("Distancia")
plt.show()

# A continuacion  se establece los ajustes de clustering jerarquico con scikit
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_clustering.fit_predict(X)


# En esta parte se visualizan los resultados mediante un grafico de matplotlib
plt.scatter(
    X[:, 0], X[:, 1], c=agg_labels, cmap="viridis", edgecolor="k", s=50 )
plt.title("Resultado del Clustering Jerarquico")
plt.xlabel("Caracteristica 1")
plt.ylabel("Caracteristica 2")
plt.show()
