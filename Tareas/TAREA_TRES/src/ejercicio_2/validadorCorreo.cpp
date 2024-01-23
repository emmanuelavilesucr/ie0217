#include "validadorCorreo.hpp"
#include <iostream>
#include <regex>


bool ValidadorCorreoElectronico::validarCorreo(const std::string& correo) {
        try {
        if (!tieneArroba(correo)) {
            throw std::invalid_argument("La direccion de correo electronico debe contener un '@'.");
        }

        std::regex formatoCorreo("^[a-zA-Z0-9.-]{1,15}@[a-zA-Z]+\\.[a-zA-Z]{2,4}$");

        if (!std::regex_match(correo, formatoCorreo)) {
            throw std::invalid_argument("La direccion de correo electronico no sigue el formato estandar.");
        }

        return true;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return false;
    }
}

bool ValidadorCorreoElectronico::tieneArroba(const std::string& correo) {
    return correo.find('@') != std::string::npos;
}