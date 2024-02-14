import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def agrupamiento(data):
     
    X = data[['selling_price', 'year', 'km_driven']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=4, random_state=42)
    data['cluster'] = kmeans.fit_predict(X_scaled)
    
    return X_scaled

