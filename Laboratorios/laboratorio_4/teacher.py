from person import Person # Esta linea importa la clase Person del modulo person

# Se crea la clase Teacher que hereda de la clase Person

class Teacher(Person):
     
     # Inicializa los atributos de la clase Teacher
     
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)    # Llama a __init__ de la clase base usando super 
        self.employee_id = employee_id 
        self.courses_taught = []   # Se crea una lista para almacenar los cursos del profesor 
       
       
     # Este metodo es el encargado de asignar los cursos que el profesor impartira
     
    def assign_courses(self, course):
        self.courses_taught.append(course)
    
    
    # Este metodo muestra la informacion del estudiante
    
    def display_info(self):
        super().display_info()   # Llama al metodo display_info de la clase base 
        
        # Muestra  la informacion del profesor
        print(f"Employee ID: {self.employee_id}\
            \nCourses taught: {' ,'.join(self.courses_taught)}\n")