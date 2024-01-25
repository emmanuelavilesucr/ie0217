class Course():
    
    # Este metodo inicializa los atributos de la clase
    
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        
    # Este metodo muestra la informacion del estudiante
    
    def display_info(self):
        
         # Muestra la informacion del curso
         
        print(f"Course code: {self.course_code}\
            \nCourse name: {self.course_name}\n")