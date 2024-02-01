import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Prestamo:
    def __init__(self, monto_prestamo, tasa_interes_anual, cuotas):
        self.monto_prestamo = monto_prestamo
        self.tasa_interes_anual = tasa_interes_anual
        self.cuotas = cuotas
        self.amortizacion = self.calcular_amortizacion()
        
              
    def calcular_amortizacion(self):
        try:
            tasa_interes_mensual = self.tasa_interes_anual / 12 / 100
            cuota_mensual = (tasa_interes_mensual * self.monto_prestamo) / (1 - (1 + tasa_interes_mensual)** -self.cuotas)
            
            saldo_restante = self.monto_prestamo
            amortizacion = []
            
            
            for cuota in range(1, self.cuotas + 1):
                interes_pendiente = saldo_restante * tasa_interes_mensual
                amortizacion_principal = cuota_mensual - interes_pendiente
                
                saldo_restante -= amortizacion_principal
                amortizacion.append({"Cuota": cuota, "Interes": interes_pendiente, "Amortizacion": amortizacion_principal, "Saldo Restante": saldo_restante})
                
            return amortizacion
            
        except ZeroDivisionError:
            print("Error: La cantidad de cuotas no puede ser cero.")
            return []
        
        
    def generar_reporte(self, archivo_salida):
        try:
            df = pd.DataFrame(self.amortizacion)
            df.to_csv(archivo_salida, index=False)
            print(f"Reporte generado con exito: {archivo_salida}")
            
        except Exception as e:
            print(f"Ocurrio un error al generar el reporte: {str(e)}")
            
            
    def graficar_amortizacion(self):
        df = pd.DataFrame(self.amortizacion)
        
        data = np.array([df["Interes"], df["Amortizacion"]])
        
        plt.bar(df["Cuota"], data[0], label="Interes")
        plt.bar(df["Cuota"], data[1], bottom = data[0], label = "Amortizacion")
        
        plt.xlabel("Numero de cuota")
        plt.ylabel("Monto ($)")
        plt.title("Amotizacion e Interes por Cuota")
        plt.legend()
        plt.show()
        
def main():
    try:
        # 1. Pedir el monto al usuario
        monto_prestamo = float(input("Ingrese el monto del prestamo: "))
    
        # 2. Pedir la tasa de interes anual (%)
        tasa_interes_anual = float(input("Ingrese la tasa de interes anual (%): "))
    
        # 3. Pedir la cantidad de cuotas
        cuotas = int(input("Ingrese la cantidad de cuotas: "))
    
        # 4. Instanciar el prestamo
        prestamo = Prestamo(monto_prestamo, tasa_interes_anual, cuotas)
    
        # 5. Generar el reporte 
        prestamo.generar_reporte("reporte_prestamo.csv")
    
        # 6. Imprimir informacion , monto, tasa, cuotas.
        print(f"Informacion del prestamo:\nMonto: ${prestamo.monto_prestamo}\nTasa de Interes Anual: {prestamo.tasa_interes_anual}%\nCuotas: {prestamo.cuotas}")
    
        # 7. Graficar la amortizacion 
        prestamo.graficar_amortizacion()
        
        # 8. Manejo de excepciones ValueError y generico 
    except ValueError as ve:
        print(f"Error de valor: {str(ve)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
 
        
        
   
    
        
