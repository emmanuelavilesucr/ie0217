import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from datos import Datos

class Grafico:
    """
    Clase encargada de toda la parte de los graficos.
    """
    def __init__(self):
        """
        Este es el metodo encargado de inicializar todos los atributos.
        """
        self.datos = Datos()  
        self.df = self.datos.obtener_datos()
        
    def visualizar(self):
        """
        En este metodo se visualizan dos tipos de graficos distintos.

        Se generan los graficos en base a los datos extraidos del archivo CSV.
        """
       
        df = self.datos.obtener_datos()
        df = self.datos.limpieza_datos()
        descripcion, contar_vuelos, detalles_pasajeros = self.datos.analisis_datos()
        
        # Configuracion del primer grafico  
        plt.figure(figsize=(8, 6))
        sns.barplot(x="Año", y="Llegadas puntuales", data=df)
        plt.title("Llegadas puntuales")
        plt.xlabel("Año")
        plt.ylabel("Llegadas puntuales")
        plt.xticks(rotation=45)
        plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: "{:,}".format(int(x)))) # Configura el formato numerico de la columna Llegadas puntuales (,)
        plt.tight_layout()
        plt.show()
        
        # Configuracion del segundo grafico 
        plt.figure(figsize=(8, 6))
        sns.lineplot(x="Año", y="Retrasos en la llegada", data=df, marker="o")
        plt.title("Retrasos en la llegada")
        plt.xlabel("Año")
        plt.ylabel("Retrasos en la llegada")
        plt.xticks(rotation=45)
        plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: "{:,}".format(int(x))))  # Configura el formato numerico de la columna del eje y (,)
        plt.tight_layout()
        plt.show()

        return
    
    
    def mostrar_tabla(self):
        """
        Metodo encargado de almacenar el DataFrame para posteriormente pasarselo al archivo main.py.
        """
        print(self.df)
