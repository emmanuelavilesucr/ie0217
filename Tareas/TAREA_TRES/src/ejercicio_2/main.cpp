#include "validadorCorreo.hpp"
#include <iostream>
#include <limits> 

int main() {
    ValidadorCorreoElectronico validador;

    bool correoValido = false;

    while (!correoValido) {
        std::string correo;
        std::cout << "Ingrese una direccion de correo electronico: ";
        std::cin >> correo;

        if (correo.empty()) {
            std::cout << "Por favor, ingrese una direccion de correo electronico." << std::endl;
        } else {
            if (validador.validarCorreo(correo)) {
                std::cout << "La direccion de correo electronico es valida." << std::endl;
                correoValido = true;
            } else {
                std::cout << "Por favor, ingrese una direccion de correo electronico valida." << std::endl;
            }
        }

        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }

    return 0;
}
