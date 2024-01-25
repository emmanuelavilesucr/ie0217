# En esta seccion se importan las clases de todos los modulos
 
from student import Student
from teacher import Teacher
from course import Course

# Se crean las instancias de Student

student1 = Student("Esteban", 43, "B30754")
student2 = Student("Maria", 28, "B35149")


# Se crean las instancias de Teacher

teacher1 = Teacher("Jorge Romero", 65, "123456")
teacher2 = Teacher("Esteban Badilla", 28, "55555")

# Se crean las instancias de Course

course1 = Course("IE0217", "DSA")
course2 = Course("IE0323", "CD1")

# Inscribe a student1 en los cursos

student1.enroll_course(course1.course_code)
student1.enroll_course(course2.course_code)

# Asigna los cursos a los profesores

teacher1.assign_courses(course1.course_code)
teacher2.assign_courses(course2.course_code)

# Finalmente, se muestra la información de student1, teacher1 y course1

student1.display_info()
teacher1.display_info()
course1.display_info()




