from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

# Se establecen la variable  X y le se asigna un dato aleatorio
np.random.seed(42)
X = np.random.rand(100, 2) * 10


silhouette_scores = []  # Lista

for k in range(2, 20):
    # Ajustes del clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)  # Calcula el puntaje de Silhoutes
    silhouette_scores.append(score)    # Agrega el puntaje a la lista
    
# Ajustes del grafico generado por matplotlib
plt.plot(range(2, 20), silhouette_scores, marker="o")
plt.title("Metodo de la Silueta")
plt.xlabel("Numero de Clusters (k)")
plt.ylabel("Coeficiente de Silueta")
plt.show()
