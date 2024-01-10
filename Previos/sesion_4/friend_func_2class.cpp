#include <iostream>
using namespace std;

class ClassB; 

class ClassA {
public:
    // Inicializando constructor de numA a 12.
    ClassA() : numA(12) {}

private:
    int numA;

    // Declaracion de funcion amiga;
    friend int add(ClassA objectA, ClassB objectB);
};

class ClassB {
public:
    // Inicializando constructor de numB a 1.
    ClassB() : numB(1) {}

private:
    int numB;

    // Declaracion de funcion amiga.
    friend int add(ClassA objectA, ClassB objectB);
};

//  Accede a los miembros de ambas clases.
int add(ClassA objectA, ClassB objectB) {
    return (objectA.numA + objectB.numB);
}

int main() {
    ClassA objectA;
    ClassB objectB;
    cout << "Sum: " << add(objectA, objectB) << endl;
    return 0;
}