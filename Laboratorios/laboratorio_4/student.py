from person import Person # Esta linea importa la clase Person del modulo person


# Se crea la clase Student que hereda de la clase Person

class Student(Person):
    
    # Este metodo esta encargado de inicializar las propiedades de la clase Student
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   # Llama al constructor de la clase base usando super 
        self.student_id = student_id
        self.courses = []
        
    # Este metodo es el encargado de inscribir el curso
    
    def enroll_course(self, course):
        self.courses.append(course)
    
    
    # Este metodo muestra la informacion del estudiante
    
    def display_info(self):
        super().display_info()   # Llama al metodo display_info de la clase base usando super
        
         # Muestra  la informacion del estudiante
        print(f"Student ID: {self.student_id}\
            \nCourses: {', '.join(self.courses)}\n")
        
        