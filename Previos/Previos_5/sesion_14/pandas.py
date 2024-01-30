import pandas as pd # Se importa la libreria de pandas 


air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv")  # Lee el archivo y almacena los datos en el DataFrame 

# Se seleccionan las columnas
air_quality_no2 = air_quality_no2[["date.utc", "location", 
                                   "parameter", "value"]]

air_quality_no2.head()  # Muestra las primeras filas del DataFrame para verificar la carga y la selección de columnas

