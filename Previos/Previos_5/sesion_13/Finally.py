# Intenta ejecutar el bloque de código
try: 
    numerator = 10
    denominator = 0

    result = numerator / denominator 
    print(result)


# Captura cualquier excepción que ocurra durante la ejecución del codigo.
except:

    print("Error: Denominator cannot be 0.")                                                                                                                                  

# Este bloque se ejecutara siempre, independientemente de si hay una excepción o no.
finally:
    print("This is finally block.")