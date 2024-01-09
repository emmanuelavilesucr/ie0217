#include <iostream>
using namespace std;

class Animal {
    public:
        void eat(){
            cout << "I can eat!" << endl;
        }

        void sleep(){
            cout << "I can sleep!" << endl;
        }
};


class Dog : public Animal { // Se crea una clase derivada de la clase base.
    public:
        void bark(){
            cout << "I can bark! Woof woof!!" << endl;
        }
};

int main() {

    Dog dog1;
    
    // Llama a los miembros de la clase base.
    dog1.eat();
    god1.sleep();
    
    // Llama a los miembros de la clase derivada.
    dog1.bark();

    return 0;
}