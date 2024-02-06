import pandas as pd
import requests

class BTS:
    def __init__(self, web):
        self.web = web 
    
    # Metodo encargado de  la obtencion de datos de las pagina web
    def obtener_datos(self):
        response = requests.get(self.web) 
        html = response.text
        
        # En esta parte implementare un cogido encargado de la extracion de los datos del HTML
        
        with open("aerolineas.csv", "w") as f:
            f.write()
            f.write()
            f.write()
        
        
        # Usar iteradores en las transformaciones a columnas
        

        return  
        
        
        
    def limpieza_datos():
        
        # Codigo relacionado con la limpieza de datos. 
        # Este metodo puede eliminar filas o columnas innecesarias, manejar valores nulos, convertir tipos de datos.
        
        return 
    
    
    def analisis_datos():
        
        # Codigo relacionado con analisis de los datos. (Mediante Pandas)
        # Este metodo esta encargado de calcular valores, identificar tendencias, encontrar patrones y buscar valores atıpicos.
        # Usar un generador para crear informes sobre la cantidad de vuelos y otro pasajeros por aerolınea.
        # Usar un iterador para filtrar datos de diferentes aerolıneas y otro iterador para recorrer el DataFrame y seleccionar solo las filas correspondientes a una aerolınea durante la limpieza.


        return 
        

bts = BTS("https://www.transtats.bts.gov/")
