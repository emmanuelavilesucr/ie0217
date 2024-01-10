#include <iostream>
using namespace std;

class ClassB; 

class ClassA {
private:
    int numA;

    // Declaracion de funcion amiga.
    friend class ClassB;

public:
    // Inicializando constructor de numA a 12.
    ClassA() : numA(12) {}
};

class ClassB {
private:
    int numB;

public:
    // Inicializando constructor de numB a 1.
    ClassB() : numB(1) {}

    int add() {
        ClassA objectA; 
        return objectA.numA + numB;
    }
};

int main() {
    ClassB objectB;
    cout << "Sum: " << objectB.add();
    return 0;
}