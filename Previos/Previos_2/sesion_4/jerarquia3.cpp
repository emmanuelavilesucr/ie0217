#include <iostream>
using namespace std;

class Animal {
    public:
        void info(){ cout << "I am an animal." << endl; }
};

class Dog : public Animal { // Clase derivada
    public:
        void bark() { cout << "I am an Dog. Woof woof." << endl; }
};

class Cat : public Animal { // Clase derivada
    public:
        void meow() { cout << "I am an Cat. Meow." << endl; }
};



int main() {
    // Creacion de un objeto de ls clase perro.
    Dog dog1;
    cout << "Dog Class" << endl;
    dog1.info(); // Funcion de la clase padre
    dog1.bark();

    // Creacion de un objeto de la clase gato.
    Cat cat1;
    cout << "\nCat Class: " << endl; // Funcion de la clase padre.
    cat1.info();
    cat1.meow();

    return 0;
}