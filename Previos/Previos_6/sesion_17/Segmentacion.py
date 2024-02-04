from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Se crea una variable encargada de guardar los datos generados en un archivo CSV mediante la biblioteca de pandas
data = pd.read_csv("data.csv")

print(data.head()) # Imprime filas del DataFrame

# Se realiza un ajuste numerico de la media y desviacion
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

inertia = []  # Se crea una lista llamada inertia

# Este ciclo for  itera sobre cada uno de los posibles valores k
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)
    
# Genera el primer grafico. (Metodo del Codo para la seleccion de k).
plt.plot(range(1, 11), inertia, marker="o")
plt.title("Metodo del Codo para Seleccion de k")
plt.xlabel("Numero de Clusters (k)")
plt.ylabel("Inercia")
plt.show()


# Se realiza la configurracion de los KMeans y clusters 
kmeans = KMeans(n_clusters=4, random_state=42)
cluster_labels = kmeans.fit_predict(scaled_data)

data["Cluster"] = cluster_labels  # Actualiza la informacion del DataFrame

# Se genera el segundo grafico.(Segmentacion de clientes por frecuencia y gasto promedio).
plt.figure(figsize=(12, 6))
for cluster in range(4):
    plt.scatter(data[data["Cluster"] == cluster] ["Frequency"],
                data[data["Cluster"] == cluster] ["Avg_spend"],
                label=f"Cluster {cluster}")     # Grafico de dispersion 
plt.title("Segmentacion de Clientes por Frecuencia y Gasto Promedio")
plt.xlabel("Frecuencia de Visita")
plt.ylabel("Gasto Promedio")
plt.legend()
plt.show()