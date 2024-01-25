class SuperClass:
    def super_method(self):
        print("Super Class method called")

# Esta clase se hereda de SuperClass

class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# Esta clase se hereda de DerivedClass1
        
class DerivedClass2(DerivedClass1):
    def derived2_method(self):
        print("Derived class 2 method called")
        
        
d2 = DerivedClass2() # Se crea la instancia 

# Se llaman a los metodos
d2.super_method()  
d2.derived1_method()
d2.derived2_method()