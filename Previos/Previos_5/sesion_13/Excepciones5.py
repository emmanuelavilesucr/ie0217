class SalaryNotRangeError(Exception):

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message) # Llama al constructor de la clase base


salary = int(input("Enter salary amount:  "))

# Verifica si el salario está en un rango deseado 
if not 5000 < salary < 15000:
    raise SalaryNotRangeError(salary)  # Lanza la excepción personalizada con el salario como argumento

