import numpy as np

np.random.seed(42)  # Voy a utilizar esta linea para que el programa sea reproductile y no aleatorio

# Declaracion de la variables globales del codigo 
materias = 5
alumnos =  5
datos = np.random.randint(0, 101, size=(alumnos, materias))

# Funcion encargada del calculo de los promedios de los estudiantes mediante uso de la biblioteca NumPy.
def promedio(datos):
    
    promedio_alumno = np.mean(datos, axis=1)
    promedio_materias = np.mean(datos, axis=0) 
    maximo = np.max(datos, axis=1)
    suma = np.sum(datos, axis=0)
    
    return 
    
# Funcion del main 
def main():
    
    promedio_alumno, promedio_materias, maximo, suma = promedio(datos) 

   
    print("Conjunto de Datos:")
    print(datos)

    print("\nResultado:")
    print("Promedio del alumno:", promedio_alumno)
    print("Promedio de la materia:", promedio_materias)
    print("Calificación mas alta:", maximo)
    print("Suma de calificaciones:", suma)
    
    
    return 
main()
    
    