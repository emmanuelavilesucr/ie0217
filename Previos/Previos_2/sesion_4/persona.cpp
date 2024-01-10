#include "persona.hpp"
using namespace std;

Persona::Persona(string nombre, int edad){
        this->nombre = nombre;   // Inicializa el atributo con el valor proporcionado.
        this->edad = edad;
}

string Persona::getNombre(){
        return nombre;       // Devuelve el valor del atributo nombre.
}

int Persona::getEdad() {
        return edad;       
}

void Persona::setEdad(int edad){
        this->edad = edad;    // Se asigna el nuevo valor proporcionado al atributo edad.
}