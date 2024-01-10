#include <iostream>
using namespace std;

class Student {
    private:
        int age;

    public:

        // Inicializando el constructor de edad a 12.
        Student() : age(12) {}

        void getAge(){
            cout << "Age = " << age << endl;
        }
};

int main(){
    
    // Declara dinamicamente el objecto Student.

    Student* ptr = new Student();

    // LLama a la funcion.
    ptr->getAge();

    // Se libera la memoria ptr.
    delete ptr;
    return 0;
}