#include "persona.hpp"
#include <iostream>
using namespace std;

int main() {
    Persona p("Juan", 25);   // Crea una instancia de la clase Persona llamada "p" con el nombre "Juan" y la edad 25.

    cout << "Nombre: " << p.getNombre() << endl;
    cout << "Edad: " << p.getEdad() << endl;

    p.setEdad(26); // Cambia la edad de la persona a 26 utilizando el método setEdad().
 
    cout << "Nueva edad: " << p.getEdad() << endl; 

    return 0; // Retorna 0 para indicar que el programa se ejecutó correctamente.

}