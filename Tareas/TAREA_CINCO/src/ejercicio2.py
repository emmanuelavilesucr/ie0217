import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Voy a utilizar esta linea para que el programa sea reproductile y no aleatorio

# Declaracion de la variables globales del codigo 
materias = 5
alumnos =  5
datos = np.random.randint(0, 101, size=(alumnos, materias))

# Funcion encargada del calculo de los promedios de los estudiantes mediante uso de la biblioteca NumPy.
def promedio(datos):
    """
    Funcion encargada de los calculos.

    @return:
        Tuple: Una tupla que contiene los datos.
    """
    
    
    promedio_alumno = np.mean(datos, axis=1)
    promedio_materias = np.mean(datos, axis=0) 
    maximo = np.max(datos, axis=1)
    suma = np.sum(datos, axis=0)
    
    return promedio_alumno, promedio_materias, maximo, suma
    
# Funcion del main 
def main():
    
    """
    Funcion main encargada de muestrar los datos y los grafico de promedios.
    """
    
    promedio_alumno, promedio_materias, maximo, suma = promedio(datos) 

    print("Conjunto de Datos:\n", datos)
    print("\nResultado:")
    print("Promedio del alumno:", promedio_alumno)
    print("Promedio de la materia:", promedio_materias)
    print("Calificación mas alta:", maximo)
    print("Suma de calificaciones:", suma)

    # Cofiguracion de los graficos de promedios
    plt.figure(figsize=(10, 5))
    plt.bar(np.arange(1, alumnos+1), promedio_alumno, color='skyblue')
    plt.title('Promedio de calificaciones por alumno')
    plt.xlabel('Alumno')
    plt.ylabel('Promedio de calificaciones')
    plt.xticks(np.arange(alumnos))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    plt.figure(figsize=(10, 5))
    plt.bar(np.arange(1, materias+1), promedio_materias, color='lightgreen')
    plt.title('Promedio de calificaciones por materia')
    plt.xlabel('Materia')
    plt.ylabel('Promedio de calificaciones')
    plt.xticks(np.arange(materias))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    
main()   