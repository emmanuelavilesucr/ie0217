/**
 * Archivo declaracion.
 **/

#ifndef PERSONA_H
#define PERSONA_H
#include <string>

using namespace std;

class Persona {
private:
    // Declara los atributos de la clase Persona.
    string nombre;
    int edad;

public:
    Persona(string nombre, int edad);   // Declara el constructor.

     // Declara los métodos públicos de la clase Persona.
    string getNombre();
    int getEdad();
    void setEdad(int edad);   
};

#endif 
