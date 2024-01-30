try:
    num = int(input("Enter a numbers: "))
    assert num % 2 == 0    # Utiliza la declaración assert para verificar que el número ingresado es par 

except:
    print("Not an even number!")

# Se ejecuta si no se produce ninguna excepción en el bloque try
else:
    reciprocal = 1/num   # Calcula el recíproco del número ingresado
    print(reciprocal)
