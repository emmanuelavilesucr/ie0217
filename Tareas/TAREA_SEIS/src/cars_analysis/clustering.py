import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def agrupamiento(data):
    """
    Esta funcion es la encargada de realizar el agrupamiento de datos utilizando el algoritmo K-means.

    :param: DataFrame que contiene los datos.
    :return: La columna 'cluster' indica la asignacion de grupo para cada punto.
    """
     
    X = data[['selling_price', 'year', 'km_driven']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=4, random_state=42)
    data['cluster'] = kmeans.fit_predict(X_scaled)
    
    return X_scaled

