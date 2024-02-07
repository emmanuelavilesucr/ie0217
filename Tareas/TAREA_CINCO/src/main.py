from grafico import Grafico
import time

def main():
    
    grafico = Grafico()
    
    while True:
        print("\n-------------Menu------------")
        print("1. Visualizar graficos")
        print("2. Ver tabla de datos")
        print("3. Salir")

        opcion = input("Ingresa una opcion: ")

        if opcion == "1":
            grafico.visualizar()
        elif opcion == "2":
            grafico.mostrar_tabla()
            time.sleep(5)
        elif opcion == "3":
            print("------Cerrando programa------")
            break  
        else:
            print("Opcion invaelida")

main()
