#include <iostream>
using namespace std;

class Base {
    public:
        virtual void print() {
            cout << "Base Function" << endl;
    }
};

class Derived : public Base {
    public:
        void print(){
            cout << "Derived Fuction" << endl;
        }
};

int main(){
    Derived derived1;
    Base * base1 = &derived1;

    // Llama a la funcion miembro de la clase derivada.
    base1->print();
    return 0;
}