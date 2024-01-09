#include <iostream>
using namespace std;

class Base {
    public:
    void print(){
        cout << "Base Function" << endl;
    }
};

class Derived : public Base { // Se crea una clase derivada usando el concepto de herencia.
    public:
    void print(){
        cout << "Derived Fuction" << endl;
    }
};

int main(){
    Derived derived1, derived2;
    derived1.print();

    // Accede  a la funcion print de la clase base. 
    derived2.Base::print();
    return 0;
}