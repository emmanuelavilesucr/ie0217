#include <iostream>
#include "estudiante.hpp"

Estudiante::Estudiante(
    const std::string& nombre, int edad
) : nombre(nombre), edad(edad) {}

void Estudiante::mostrarDatos() {
    std::cout << "Nombre: " << nombre;
    std::cout << ", Edad: " << edad << std::endl;
}