class InvalidAgeException(Exception):
    pass

number = 18

try:

    input_num = int(input("Enter a number: "))
    
    # Verifica si el número ingresado es menor que number
    if input_num < number:
        raise InvalidAgeException

    else:
        print("Eligible to vote")

# Captura la excepción y maneja el caso donde el número es menor que number
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
