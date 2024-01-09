#include <iostream>
using namespace std;

class Animal {
    public:
        void setEdad(int age){
            edad = age;
        }

        int getEdad(){
            return edad;
        }

    protected:
        string nombre;

    private:
        int edad;
};

class Perro : public Animal {
    public:
        void setNombre(string n){
            nombre = n;
        }
        string getNombre(){
            return nombre;
        }
};

int main(){
    Perro miPerro;
    miPerro.setNombre("Toby");
    miPerro.setEdad(3);

    cout << "Mi perro se llama " << miPerro.getNombre() << endl;
    cout << "y tiene " << miPerro.getEdad() << " anios. " << endl;

    return 0;
}

