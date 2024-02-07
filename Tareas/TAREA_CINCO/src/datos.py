import pandas as pd

class Datos:
    """
    Clase encargada de la mapinulacion de los datos del archivo CSV.
    """
    def __init__(self):

        self.df = None
        self.columnas = ["Año", "Llegadas puntuales", "A tiempo (%)", "Retrasos en la llegada", "Demorado (%)", "Vuelo cancelado", "Cancelado (%)", "desviado", "Las operaciones de vuelo"]
      
    def obtener_datos(self):
        """
        Este metodo es el encargado de obtener los datos del archivo CSV.

        @return:
            pd.DataFrame: Carga los datos del CSV.
        """
        try:
            self.df = pd.read_csv("aerolineas.csv", delimiter=",", header=None, names=self.columnas)
            print(self.df.head())  
        except FileNotFoundError:
            print("El archivo no se encontro.")
        except Exception as e:
            print("Ocurrio un error durante la carga de datos:", str(e))

        for columna in self.columnas:
            if self.df[columna].dtype == "object": 
                self.df[columna] = pd.to_numeric(self.df[columna].str.replace(".", " ").str.replace(",", "."))

        return self.df

    def limpieza_datos(self): 
        """
        Este metodo es empleado en la limpieza de los datos mediante la eliminacion de columnas innecesarias y filas con valores nulos.

        @return:
            pd.DataFrame: Limpia los datos.
        """                 
        columnas_innecesarias = ["Demorado (%)", "Vuelo cancelado", "Cancelado (%)", "desviado"]
        self.df.drop(columns=columnas_innecesarias, inplace=True)
        self.df.dropna(inplace=True)
        
        return self.df
    
    def analisis_datos(self):
        """
        Generador encargado de contar los vuelos.

        @return: tupla.
        """
                
        descripcion = self.df.describe()
        def contar_vuelos_por_aerolinea():
            for aerolinea in self.df["Año"].unique():
                yield aerolinea, len(self.df[self.df["Año"] == aerolinea])
        
        def obtener_detalles_pasajeros_por_aerolinea():
            """
            Generador encargado de obtener detalles.

            @return: tupla.
            """  
            for aerolinea in self.df["Año"].unique():
                detalles = self.df[self.df["Año"] == aerolinea]["Llegadas puntuales"].describe()
                yield aerolinea, detalles
        
        return descripcion, contar_vuelos_por_aerolinea(), obtener_detalles_pasajeros_por_aerolinea()

