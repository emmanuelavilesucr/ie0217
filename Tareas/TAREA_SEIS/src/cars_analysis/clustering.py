from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def agrupamiento(X, n_clusters=4):
    scaler = StandardScaler()
    X_normalizado = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    
    return kmeans.fit_predict(X_normalizado)
