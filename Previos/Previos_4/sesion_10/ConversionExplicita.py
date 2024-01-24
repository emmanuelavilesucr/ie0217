num_string = "12"  # Asigna un string a la variable
num_integer = 23   # Asigna un numero entero a la variable
 
# Imprime el tipo de datos de num_string antes de la conversión

print("Data type of num_string before Type Casting: ", type(num_string))

num_string = int(num_string)

print("Data type of num_string after Type Casting:", type(num_string))

num_sum = num_integer + num_string

# Imprime la suma y el tipo de datos del resultado

print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))