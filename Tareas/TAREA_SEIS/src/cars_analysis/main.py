import os
import pandas as pd
from regression import regresion_lineal, regresion_polinomial, categorias
from clustering import agrupamiento
from kaggle.api.kaggle_api_extended import KaggleApi
import matplotlib.pyplot as plt

def main():
    
    api = KaggleApi()
    api.authenticate()
    dataset_name = "akshaydattatraykhare/car-details-dataset"
    api.dataset_download_files(dataset_name, path="./Datos", unzip=True)
    
    data = pd.read_csv('./Datos/CAR DETAILS FROM CAR DEKHO.csv')
    
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    categorias(data)
    regresion_lineal(data)
    regresion_polinomial(data)
    agrupamiento(data)
    X_scaled = agrupamiento(data)
    
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2], c=data['cluster'], cmap='viridis')
    ax.set_xlabel('Precio de venta')
    ax.set_ylabel('Año')
    ax.set_zlabel('Kilometros recorridos')
    plt.title('Vehículos')
    plt.show()


main()
