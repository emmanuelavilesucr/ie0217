import timeit
import cProfile

from alergia import Alergia
from evaluacion import EvaluacionEspecifica
from tipos_alergias import TiposAlergias
from evaluacion_general import EvaluacionGeneral

def interfaz_usuario():
    tipos_alergias = TiposAlergias()
    evaluacion_especifica = EvaluacionEspecifica()
    evaluacion_general = EvaluacionGeneral(evaluacion_especifica)
    tipos_alergias.cargar_alergias_desde_archivo("Alergias.txt")

    while True:
        print("Menu:")
        print("1. Calcular alergias especificas")
        print("2. Ingresar alergias y puntajes")
        print("3. Salir")

        opcion = input("Ingrese la opcion (1, 2 o 3): ")

        if opcion == "1":
            puntuacion_general = int(input("Ingrese la puntuacion general de alergias: "))
            evaluacion_especifica.imprimir_evaluacion(puntuacion_general)

        elif opcion == "2":
            entrada_usuario = input("Ingrese el nombre o valor de la alergia (o 'fin' para terminar): ")
            while entrada_usuario.lower() != 'fin':
                alergia = tipos_alergias.analizar_entrada_usuario(entrada_usuario)
                if alergia:
                    evaluacion_especifica.alergias.append(alergia)
                    evaluacion_general.alergias_evaluadas.append(alergia)
                else:
                    print("Entrada no valida. Intente nuevamente.")
                entrada_usuario = input("Ingrese el nombre o valor de la alergia (o 'fin' para terminar): ")

        elif opcion == "3":
            print("Saliendo del programa.")

            break

        else:
            print("Opción no valida. Intente nuevamente.")
    evaluacion_general.imprimir_resultados()


def medir_tiempo():

    """
    Mide el tiempo de ejecución de la función interfaz_usuario utilizando timeit.
    """
    
    setup_code = """
from __main__ import interfaz_usuario
"""
    timeit_code = "interfaz_usuario()"

    tiempo = timeit.timeit(stmt=timeit_code, setup=setup_code, number=1)
    print(f"Tiempo de ejecución: {tiempo} segundos")

def realizar_perfilado():

    """
    Realiza el perfilado de la función interfaz_usuario utilizando cProfile.
    """
    
    cProfile.run("interfaz_usuario()", sort="cumulative")

medir_tiempo()
realizar_perfilado()

