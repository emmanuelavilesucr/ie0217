import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from datos import Datos

class Grafico:
    def __init__(self):
        self.datos = Datos()  
        self.df = self.datos.obtener_datos()
        
    def visualizar(self):
       
        df = self.datos.obtener_datos()
        df = self.datos.limpieza_datos()
        descripcion, contar_vuelos, detalles_pasajeros = self.datos.analisis_datos()
        
        plt.figure(figsize=(8, 6))
        sns.barplot(x="Año", y="Llegadas puntuales", data=df)
        plt.title("Llegadas puntuales")
        plt.xlabel("Año")
        plt.ylabel("Llegadas puntuales")
        plt.xticks(rotation=45)
        plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: "{:,}".format(int(x))))
        plt.tight_layout()
        plt.show()
        

        plt.figure(figsize=(8, 6))
        sns.lineplot(x="Año", y="Retrasos en la llegada", data=df, marker="o")
        plt.title("Retrasos en la llegada")
        plt.xlabel("Año")
        plt.ylabel("Retrasos en la llegada")
        plt.xticks(rotation=45)
        plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: "{:,}".format(int(x))))
        plt.tight_layout()
        plt.show()

        return
    
    
    def mostrar_tabla(self):
    
        print(self.df)
