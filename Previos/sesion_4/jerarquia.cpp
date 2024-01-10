#include <iostream>
using namespace std;


class A {
    public:
        void display(){  // Método para mostrar contenido de la clase base.
            cout << "Base class content.";
        }
};

class B : public A {}; // Clase B hereda públicamente de la clase A.

class C : public B {}; 

int main() {
    C obj;  // Creando un objeto de la clase C.
    obj.display();
    return 0;
}